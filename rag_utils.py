import os
import json
import google.generativeai as genai
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

FAISS_PATH = "faiss_store"
METADATA_PATH = "metadata/uploaded_files.json"

os.makedirs("metadata", exist_ok=True)

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash-lite")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}
)

def load_uploaded_files():
    if not os.path.exists(METADATA_PATH):
        return []
    with open(METADATA_PATH, "r") as f:
        return json.load(f).get("files", [])

def save_uploaded_file(filename):
    files = load_uploaded_files()
    if filename not in files:
        files.append(filename)
        with open(METADATA_PATH, "w") as f:
            json.dump({"files": files}, f)

def create_rag_chain(chunks=None, filename=None):

    if os.path.exists(os.path.join(FAISS_PATH, "index.faiss")):
        vector_store = FAISS.load_local(
            FAISS_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )
    else:
        vector_store = FAISS.from_texts([], embeddings)

    if chunks:
        vector_store.add_texts(chunks)
        vector_store.save_local(FAISS_PATH)
        if filename:
            save_uploaded_file(filename)

    retriever = vector_store.as_retriever()

    def qa(query: str):
        questions = [q.strip() for q in query.split(" and ")]
        answers = []

        for q in questions:
            docs = retriever.invoke(q)
            context = "\n\n".join(doc.page_content for doc in docs)

            prompt = f"""
            Answer only from the context below.

            Context:
            {context}

            Question:
            {q}
            """

            response = model.generate_content(prompt)
            answers.append(f" {q} : {response.text}")

        return "\n\n".join(answers)

    return qa
