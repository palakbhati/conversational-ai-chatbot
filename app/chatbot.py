from langchain_community.llms import Ollama
from langchain_community.chat_message_histories import ChatMessageHistory
import pandas as pd
from pypdf import PdfReader

# Load local Mistral model
llm = Ollama(model="mistral")

# In-memory chat history
chat_history = ChatMessageHistory()


def get_response(user_input: str) -> str:
    chat_history.add_user_message(user_input)

    response = llm.invoke(chat_history.messages)

    chat_history.add_ai_message(response)

    return response


def read_file(uploaded_file):

    if uploaded_file.name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:  # Prevent None error
                text += page_text

        return text[:5000]   # Limit size (important)

    elif uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")[:5000]

    elif uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
        return df.to_string()[:5000]

    else:
        return "Unsupported file type"


def analyze_document(text, question):

    prompt = f"""
You are an AI assistant.
Analyze the following document and answer clearly.

Document:
{text}

Question:
{question}
"""

    response = llm.invoke(prompt)
    return response
