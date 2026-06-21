from dotenv import load_dotenv

from rag.loader import PDFLoader
from rag.splitter import split_documents
from rag.vectorstore import create_vector_store
from rag.retriever import get_retriever
from rag.llm import get_llm

load_dotenv()

# Load PDF
pdf_loader = PDFLoader()

documents = pdf_loader.load_pdf("./data/pdfs/employee_handbook.pdf")

chunks = split_documents(documents)

vector_store = create_vector_store(chunks)

retriever = get_retriever(vector_store)

# Question
question = "What is the refund policy?"

# Retrieve relevant docs
docs = retriever.invoke(question)

context = "\n\n".join(
    doc.page_content for doc in docs
)

# Build prompt
prompt = f"""
Answer the question using ONLY the context below.

Context:
{context}

Question:
{question}
"""

llm = get_llm()

response = llm.invoke(prompt)

print("\nAnswer:\n")

print(response.content)