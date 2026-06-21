from dotenv import load_dotenv

from rag.loader import PDFLoader
from rag.splitter import split_documents
from rag.vectorstore import create_vector_store
from rag.chain import RAGChain

load_dotenv()

loader = PDFLoader()

documents = loader.load_pdf(
    "./data/pdfs/employee_handbook.pdf"
)

chunks = split_documents(documents)

vector_store = create_vector_store(chunks)

rag_chain = RAGChain(vector_store)

response1 = rag_chain.ask(
    "What is the leave policy?"
)

print("\nQ1:")
print(response1["answer"])

response2 = rag_chain.ask(
    "Can they be carried forward?"
)

print("\nQ2:")
print(response2["answer"])