import streamlit as st
from agent.chatbot_agent import get_agent

st.set_page_config(page_title="AI Agent Chatbot")
st.title("🤖 HuggingFace AI Agent Chatbot")

if 'agent' not in st.session_state:
    st.session_state.agent = get_agent()
    st.session_state.chat_history = []

user_input = st.chat_input("Ask me anything...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))
    with st.spinner("Thinking..."):
        try:
            response = st.session_state.agent.run(user_input)
            st.session_state.chat_history.append(("agent", response))
        except Exception as e:
            response = f"Error: {str(e)}"
            st.session_state.chat_history.append(("agent", response))

for role, msg in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(msg)