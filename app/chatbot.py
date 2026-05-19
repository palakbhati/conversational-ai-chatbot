from groq import Groq
from langchain_community.chat_message_histories import ChatMessageHistory
import pandas as pd
from pypdf import PdfReader
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Memory
chat_history = ChatMessageHistory()


def get_response(user_input: str) -> str:

    # Store user message
    chat_history.add_user_message(user_input)

    # Convert memory into Groq message format
    messages = []

    for msg in chat_history.messages:
        if msg.type == "human":
            messages.append({
                "role": "user",
                "content": msg.content
            })
        else:
            messages.append({
                "role": "assistant",
                "content": msg.content
            })

    # Generate response
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=1,
        max_completion_tokens=1024,
        top_p=1
    )

    response = completion.choices[0].message.content

    # Store AI response
    chat_history.add_ai_message(response)

    return response


def read_file(uploaded_file):

    if uploaded_file.name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

        return text[:5000]

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

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1
    )

    response = completion.choices[0].message.content

    return response