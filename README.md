# 📄 RAG Resume Chatbot

A local chatbot to answer questions from uploaded PDF resumes using RAG, LangChain, and Mistral LLM (via Ollama).

## 🚀 Features
- Upload multiple PDF resumes
- Ask questions like “Who knows Python?”
- Answers generated from actual resume data
- Fully offline – no OpenAI key required

## 🛠️ Tech Stack
- **Streamlit** – Frontend web UI
- **LangChain** – RAG framework (Retriever + LLM)
- **Ollama + Mistral** – Local LLM for embedding + answering
- **FAISS** – Vector DB for semantic search
- **PyPDFLoader** – To read PDF files
- **OllamaEmbeddings** – To convert text to vectors

## 📦 Installation
```bash
pip install -r requirements.txt
