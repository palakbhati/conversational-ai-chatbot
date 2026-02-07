import streamlit as st
from chatbot import get_response, read_file, analyze_document

st.set_page_config(page_title="Conversational AI Chatbot", layout="centered")

st.title("🧠 Conversational AI with Contextual Memory")

# File Upload Section
uploaded_file = st.file_uploader("Upload PDF, TXT or CSV", type=["pdf","txt","csv"])

if uploaded_file:
    file_text = read_file(uploaded_file)
    st.success("File uploaded successfully!")

    file_question = st.text_input("Ask something about the file")

    if file_question:
        answer = analyze_document(file_text, file_question)
        st.write(answer)

st.divider()

# Chat Section
if "chat" not in st.session_state:
    st.session_state.chat = []

for role, message in st.session_state.chat:
    if role == "user":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**Bot:** {message}")

user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.chat.append(("user", user_input))
    response = get_response(user_input)
    st.session_state.chat.append(("bot", response))
    st.rerun()
