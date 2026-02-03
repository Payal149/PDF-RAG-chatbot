# PDF RAG Chatbot (Streamlit + FAISS + Gemini)

A **Retrieval-Augmented Generation (RAG)** chatbot that allows you to upload PDFs once, store their content persistently using **FAISS**, and ask questions anytime.
The chatbot answers **only from the uploaded documents** using Google Gemini.


##  Features

* Upload PDF files only once
* Persistent document storage using FAISS
* Ask unlimited questions without re-uploading PDFs
* Answers are generated strictly from document content
* Supports asking multiple questions one after another
* Simple and clean Streamlit UI
* Tracks uploaded PDFs internally


##  How It Works

1. PDF files are uploaded and read
2. Text is split into chunks
3. Chunks are converted into embeddings
4. All embeddings are stored in a single FAISS vector store
5. On every question:

   * Relevant chunks are retrieved
   * Gemini generates an answer using only that context


## Project Structure

```
rag-pdf-chatbot/
│
├── app.py
├── pdf_utils.py
├── rag_utils.py
├── requirements.txt
├── .env
├── .gitignore
│
├── faiss_store/
│   └── index.faiss
│
└── metadata/
    └── uploaded_files.json
```


## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/PDF-RAG-chatbot.git
cd PDF-RAG-chatbot
```

###  Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

###  Install Dependencies

```bash
pip install -r requirements.txt
```


##  Environment Setup

Create a `.env` file in the project root:

```
GOOGLE_API_KEY=your_google_gemini_api_key
```

> `.env` is ignored by Git for security.


## Run the Application

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```


##  Example Questions

* What is the HR name?
* What is the joining date?
* What is mentioned in the offer letter?
* Give employee details

You can ask **multiple questions one after another** without re-uploading PDFs.


##  Security

* API keys are stored securely using `.env`
* FAISS index and metadata are stored locally
* No document data is exposed publicly


##  Notes

* Free Gemini API has request limits
* Large PDFs may take time during first upload
* Answers are limited to document context only


##  Author

**Payal**

Built as a learning and portfolio project for RAG-based AI systems.


##  Support

If you find this project useful, give it a ⭐ on GitHub.



