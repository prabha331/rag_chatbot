import streamlit as st
import os
from rag_engine import create_vectorstore, qa_bot

st.title("Resume RAG Chatbot")

pdf_folder = "pdfs"

uploaded_files = st.file_uploader("Upload Resume PDFs", accept_multiple_files=True, type=["pdf"])
if uploaded_files:
    os.makedirs(pdf_folder, exist_ok=True)
    for uploaded_file in uploaded_files:
        with open(os.path.join(pdf_folder, uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
    create_vectorstore(pdf_folder)
    st.success("Vectorstore created successfully!")

query = st.text_input("Ask about a candidate:")
if query:
    response = qa_bot(query)
    st.write("Answer:", response)
