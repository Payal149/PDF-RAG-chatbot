from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_split_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
            
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    
    chunks = splitter.split_text(text)
    return chunks