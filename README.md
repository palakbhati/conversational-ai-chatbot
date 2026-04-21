# Conversational AI Chatbot with Contextual Memory

An AI-powered conversational chatbot built using **LangChain**, **Streamlit**, and a local **Phi-3 Mini LLM (via Ollama)**.
The system enables human-like, context-aware interactions and can also analyze uploaded documents.
The entire project runs **offline** with **zero API cost**, ensuring privacy and accessibility.

---

## Features

- Context-aware multi-turn conversations
- Memory management using **ChatMessageHistory**
- Local LLM integration using **Mistral via Ollama**
- Upload and analyze **PDF, TXT, and CSV** files
- Streamlit-based interactive UI
- Fully offline execution (no paid APIs)

---

## Tech Stack

- **Python**
- **LangChain**
- **Streamlit**
- **Ollama (Mistral Model)**
- **Pandas**
- **PyPDF**

---

## Project Structure

```
conversational-ai-chatbot/
│
├── app/
│   ├── app.py        # Streamlit UI
│   └── chatbot.py    # LLM + Memory + File Analysis Logic
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### 1. Clone Repository

```
git clone https://github.com/palakbhati/conversational-ai-chatbot.git
cd conversational-ai-chatbot
```

### 2. Create Virtual Environment

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Install Ollama & Download Model

Install Ollama from: [https://ollama.com](https://ollama.com)

Then run:

```
ollama pull Phi-3 Mini
```

---

## Run the Application

```
streamlit run app/app.py
```

---

## Usage

- Chat with the AI using contextual memory
- Upload documents (PDF, TXT, CSV)
- Ask questions or request summaries
- The chatbot recalls previous conversation context

---

## How Memory Works

The chatbot uses **LangChain’s ChatMessageHistory** to store previous user and assistant messages.
These messages are passed to the language model during each interaction, enabling contextual, multi-turn conversations.

---

## Limitations

- Large documents may be slow due to local model constraints
- Currently uses short-term in-memory storage
- Performance depends on system hardware

---

## Future Improvements

- Long-term memory storage
- Document chunking and embeddings (RAG)
- Voice-based interaction
- Deployment optimization

---

## Author

Developed as a hands-on project to explore **Generative AI, LLMs, and conversational memory systems** using fully free and open-source tools.
