from utils import execute_mysql_query, execute_neo4j_query, load_ticker_mapping, get_ticker_from_name
from langchain_components import conversation_chain, mysql_prompt_template, neo4j_prompt_template, conversation_memory
from config import llm

# Load the ticker mapping once
ticker_mapping = load_ticker_mapping()

# Define custom memory for company-specific data
custom_memory = {"company_name": None, "ticker": None}

def rephrase_query(user_query):
    prompt = f"Rephrase the following query for clarity:\n\n'{user_query}'"
    rephrased_query = llm.predict(prompt)
    return rephrased_query.strip()

def select_and_generate_query(input_text):
    if "sentiment" in input_text.lower() or "analysis" in input_text.lower():
        prompt_template = neo4j_prompt_template
    else:
        prompt_template = mysql_prompt_template

    prompt = prompt_template.format(input=input_text)
    return llm.predict(prompt)

def transform_query(user_query, structured_query):
    if "more details" in user_query.lower() or "more data" in user_query.lower():
        if "LIMIT" in structured_query:
            structured_query = structured_query.replace("LIMIT 30", "LIMIT 100")
    return structured_query

def reconstruct_query(user_query, last_query, last_result):
    if "specific dates" in user_query.lower() and isinstance(last_result, list):
        dates = [record["date"] for record in last_result if "date" in record]
        if dates:
            prompt = (
                f"Based on the following dates {dates}, create a query that retrieves information"
                f" for these specific dates from the database."
            )
            reconstructed_query = llm.predict(prompt)
            return reconstructed_query.strip()
    elif "more details" in user_query.lower():
        return transform_query(user_query, last_query)
    return last_query

def update_custom_memory(company_name=None, ticker=None):
    if company_name:
        custom_memory["company_name"] = company_name
    if ticker:
        custom_memory["ticker"] = ticker

def run_pipeline(user_query, company_name=None):
    if not company_name:
        company_name = custom_memory.get("company_name")
        if not company_name:
            return "Please specify a company name."

    ticker = get_ticker_from_name(company_name, ticker_mapping)
    if not ticker:
        return f"Ticker not found for company '{company_name}'. Please check the company name."
    
    update_custom_memory(company_name=company_name, ticker=ticker)

    last_query = conversation_memory.load_memory_variables({}).get("last_query")
    last_result = conversation_memory.load_memory_variables({}).get("last_result")

    if last_query and last_result and ("follow up" in user_query.lower() or "it" in user_query.lower()):
        structured_query = reconstruct_query(user_query, last_query, last_result)
    else:
        refined_query = rephrase_query(user_query)
        structured_query = select_and_generate_query(refined_query)

    if "SELECT" in structured_query.upper():
        result = execute_mysql_query(structured_query)
    elif "MATCH" in structured_query.upper():
        result = execute_neo4j_query(structured_query)
    else:
        result = "Unable to determine the appropriate data source."

    conversation_memory.save_context(
        {"input": user_query}, 
        {"output": result, "last_query": structured_query, "last_result": result}
    )

    response = conversation_chain.predict(input=user_query)
    return response

# Function to reset the conversation and memory
def reset_memory():
    # Clear custom memory
    custom_memory["company_name"] = None
    custom_memory["ticker"] = None
    
    # Clear conversation memory
    conversation_memory.clear()

    print("Conversation and memory have been reset.")
