# 🧠 Conversational AI Chatbot with Contextual Memory

> A context-aware AI chatbot built with **Groq**, **LangChain**, and **Streamlit** — featuring multi-turn memory and document analysis for PDF, TXT, and CSV files.
---

## 🌐 Live Demo

Try it out → [conversational-ai-chatbot on Streamlit](https://conversational-ai-chatbot-gmeioqynvpgg2zi8hc2aso.streamlit.app/)

---

## 📌 Overview

This project is a **conversational AI assistant** that remembers the context of your conversation across multiple turns. It uses the **Groq API** to run **Meta's LLaMA 3.1 8B Instant** model — a fast, powerful LLM — and wraps it with **LangChain's `ChatMessageHistory`** to maintain dialogue context.

Beyond chat, users can upload a document (PDF, TXT, or CSV) and ask questions directly about its contents — all through a clean **Streamlit** interface.

---

## ✨ Features

- **Multi-turn contextual conversation** — the bot remembers the full chat history within a session
- **Groq-powered LLM** — uses `llama-3.1-8b-instant` for fast, high-quality responses
- **Document Q&A** — upload a file and ask questions about it separately from the main chat
- **Supports PDF, TXT, and CSV** — extracts and analyzes up to 5,000 characters of content
- **Session-based chat history** — messages persist across reruns using `st.session_state`
- **Simple, clean UI** — built entirely with Streamlit

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| LLM Provider | Groq API |
| LLM Model | `llama-3.1-8b-instant` (Meta LLaMA 3.1 8B) |
| Memory | LangChain `ChatMessageHistory` |
| UI | Streamlit |
| PDF Parsing | PyPDF |
| CSV/Data Handling | Pandas |

---

## 📁 Project Structure

```
conversational-ai-chatbot/
│
├── app/
│   ├── app.py          # Streamlit UI, file upload, session state, chat interface
│   └── chatbot.py      # Groq client, memory management, file reading, document analysis
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ How It Works

### 🗣️ Conversational Memory

`chatbot.py` uses LangChain's `ChatMessageHistory` to store every user and assistant message. On each new user input, the **entire conversation history** is sent to the Groq API, allowing the model to reference anything said earlier in the session.

```
You:  "What is gradient descent?"
Bot:  "Gradient descent is an optimization algorithm..."

You:  "Can you give a simpler explanation?"   ← refers to previous context
Bot:  "Sure! Think of it like rolling a ball downhill..."  ← remembers the topic
```

### 📄 Document Analysis

Document Q&A is handled **separately** from the main chat. When a file is uploaded:

1. `read_file()` extracts up to **5,000 characters** from the document
2. The extracted text and user's question are combined into a structured prompt
3. The prompt is sent to Groq as a **one-shot query** (independent of chat memory)
4. The answer is displayed directly below the question

| File Type | Extraction Method |
|---|---|
| PDF | `PdfReader` from PyPDF — extracts text page by page |
| TXT | Decoded as UTF-8 string |
| CSV | Read with Pandas and converted to a string table |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- A free [Groq API key](https://console.groq.com/)

### 1. Clone the Repository

```bash
git clone https://github.com/palakbhati/conversational-ai-chatbot.git
cd conversational-ai-chatbot
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Your Groq API Key

Create a `.streamlit/secrets.toml` file in the project root:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

> Get your free API key from [console.groq.com](https://console.groq.com/)

### 5. Run the App

```bash
streamlit run app/app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 🖥️ UI Walkthrough

```
┌──────────────────────────────────────────────────┐
│  🧠 Conversational AI with Contextual Memory     │
│                                                  │
│  [ Upload PDF, TXT or CSV ]                      │  ← File uploader
│  [ Ask something about the file... ]             │  ← Document Q&A input
│  ────────────────────────────────────────────    │  ← Divider
│  You: Hello!                                     │  │
│  Bot: Hi! How can I help you today?              │  │  ← Chat history
│  You: Tell me about LLMs                         │  │     (session state)
│  Bot: LLMs are large language models...          │  │
│                                                  │
│  [ Type your message here... ]                   │  ← Chat input
└──────────────────────────────────────────────────┘
```

---

## ⚠️ Limitations

- Chat memory is **session-scoped** — it resets when the app restarts
- Document analysis reads only the **first 5,000 characters** of uploaded files
- Document Q&A is **independent of chat memory** — the bot won't recall file content in the main chat
- Requires an active internet connection to reach the Groq API

---

## 🔭 Roadmap

- [ ] Integrate document content into the main chat memory (RAG pipeline)
- [ ] Support larger documents with chunking and embeddings
- [ ] Persistent memory across sessions (database or vector store)
- [ ] Add support for DOCX and image files
- [ ] Voice input/output
- [ ] Chat export (download conversation as PDF or TXT)

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push and open a Pull Request

---

## 👩‍💻 Author

**Palak Bhati**

Built as a hands-on project to explore conversational AI, LLM memory management, and document analysis using LangChain, Groq, and Streamlit.

---

## 📄 License

This project is licensed under the MIT License.
