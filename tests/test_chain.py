from dotenv import load_dotenv

from rag.loader import PDFLoader
from rag.splitter import split_documents
from rag.vectorstore import create_vector_store
from rag.chain import RAGChain

load_dotenv()

pdf_loader = PDFLoader()

documents = pdf_loader.load_pdf("./data/pdfs/employee_handbook.pdf")

chunks = split_documents(documents)

vector_store = create_vector_store(chunks)

rag_chain = RAGChain(vector_store)

question = "What is the refund policy?"

answer = rag_chain.ask(question)

print("\nAnswer:\n")

print(answer["answer"])

print("\nSources:\n")

for doc in answer["sources"]:
    print(
        f"Page: {doc.metadata.get('page', 'Unknown') + 1}"
    )