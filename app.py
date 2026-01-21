import streamlit as st
from pdf_utils import load_and_split_pdf
from rag_utils import create_rag_chain, load_uploaded_files

st.title("PDF RAG Chatbot")

uploaded_files = load_uploaded_files()

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    filename = uploaded_file.name
    if filename in uploaded_files:
        st.info("File already uploaded")
    else:
        with st.spinner("Processing document..."):
            chunks = load_and_split_pdf(uploaded_file)
            st.session_state.qa_chain = create_rag_chain(chunks, filename)
        st.success("Document added successfully")

if uploaded_files:
    if "qa_chain" not in st.session_state:
        st.session_state.qa_chain = create_rag_chain()

    question = st.text_input("Ask a question")

    if question:
        answer = st.session_state.qa_chain(question)
        st.write(answer)
else:
    st.info("Upload at least one PDF to ask questions")
