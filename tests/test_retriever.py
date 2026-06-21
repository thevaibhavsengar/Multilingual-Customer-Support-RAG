from dotenv import load_dotenv

from rag.loader import PDFLoader
from rag.splitter import split_documents
from rag.vectorstore import create_vector_store
from rag.retriever import get_retriever

load_dotenv()

pdf_loader = PDFLoader()

documents = pdf_loader.load_pdf("./data/pdfs/employee_handbook.pdf")

chunks = split_documents(documents)

vector_store = create_vector_store(chunks)

retriever = get_retriever(vector_store)

query = "What is the refund policy?"

results = retriever.invoke(query)

print("\nRetrieved Chunks:\n")

for i, doc in enumerate(results, start=1):
    print(f"\nResult {i}")
    print("-" * 50)
    print(doc.page_content)