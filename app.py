import streamlit as st
import pandas as pd
from streamlit_chat import message
from pipeline import run_pipeline, reset_memory

# Load company names for the dropdown
stock_data = pd.read_csv("../pre-analysis/datasets/stock_name_ticker.csv")
company_names = stock_data["company_name"].unique()

# Initialize session state variables for company name and messages
if "company_name" not in st.session_state:
    st.session_state.company_name = ""
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! How can I assist you today?"}]

# Sidebar for selecting the company
selected_company = st.sidebar.selectbox("Select Company", [""] + list(company_names))
if selected_company:
    st.session_state.company_name = selected_company

# # Sidebar buttons for "End Conversation" and "Reset"
# if st.sidebar.button("End Conversation"):
#     reset_memory() 
#     st.session_state.messages = [{"role": "assistant", "content": "Hello! How can I assist you today?"}]
#     st.experimental_rerun()

if st.sidebar.button("Reset"):
    reset_memory() 
    st.session_state.messages = [{"role": "assistant", "content": "Hello! How can I assist you today?"}]
    st.session_state.company_name = ""
    st.experimental_rerun()

# Display chat history using streamlit-chat
st.title("StockChat")
for message_data in st.session_state.messages:
    message(message_data["content"], is_user=(message_data["role"] == "user"))

# Inject JavaScript for auto-scrolling
scroll_js = """
<script>
    var chatDiv = window.parent.document.getElementById('root');
    chatDiv.scrollTop = chatDiv.scrollHeight;
</script>
"""
st.components.v1.html(scroll_js, height=0)

# Input box for user query with a unique key each time, to simulate clearing
user_input = st.text_input("Type your question here...", key=f"input_{len(st.session_state.messages)}")
send_button = st.button("Send")

# Check if user has input a message and clicked the send button
if send_button and user_input:
    # Add user's message to session state
    st.session_state.messages.append({"role": "user", "content": user_input})
    message(user_input, is_user=True)  # Display the user message immediately

    # Generate assistant response with a typing indicator
    with st.spinner("StockChat is typing..."):
        if st.session_state.company_name:
            response = run_pipeline(user_input, st.session_state.company_name)
        else:
            response = "Please select a company from the sidebar to proceed."

    # Add assistant's response to session state
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Trigger a rerun to refresh the input box and scroll to the bottom
    st.experimental_rerun()
