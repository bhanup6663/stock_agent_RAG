from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import ChatPromptTemplate
from config import llm

conversation_memory = ConversationBufferMemory(memory_key="chat_history")
conversation_prompt = ChatPromptTemplate.from_template("""
Assistant is a financial data assistant with access to stock data and sentiment analysis.

Chat history:
{chat_history}

User's question: {input}

Assistant's response:
""")
conversation_chain = ConversationChain(llm=llm, memory=conversation_memory, prompt=conversation_prompt)

mysql_prompt_template = ChatPromptTemplate.from_template(
    "Translate the following natural language request into an SQL query:\n\n'{input}'"
)

neo4j_prompt_template = ChatPromptTemplate.from_template(
    "Translate the following natural language request into a Cypher query:\n\n'{input}'"
)
