from dotenv import load_dotenv

from rag.loader import PDFLoader
from rag.splitter import split_documents
from rag.vectorstore import create_vector_store

load_dotenv()

pdf_loader = PDFLoader()

documents = pdf_loader.load_pdf("./data/pdfs/employee_handbook.pdf")

chunks = split_documents(documents)

vector_store = create_vector_store(chunks)

print("FAISS Index Created Successfully!")

print(f"Documents: {len(documents)}")
print(f"Chunks: {len(chunks)}")