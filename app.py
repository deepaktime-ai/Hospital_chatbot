import streamlit as st
from agent import Agent

st.set_page_config(page_title="Hospital Chatbot")

st.title("🏥 Hospital AI Assistant")

agent = Agent()

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("Ask your question:")

if st.button("Send"):
    if user_input:
        response = agent.run(user_input)

        st.session_state.chat.append(("You", user_input))
        st.session_state.chat.append(("Bot", response))

for role, msg in st.session_state.chat:
    if role == "You":
        st.write(f"🧑 {msg}")
    else:
        st.write(f"🤖 {msg}")