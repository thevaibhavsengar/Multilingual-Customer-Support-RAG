from rag.loader import PDFLoader
from rag.splitter import split_documents

pdf_loader = PDFLoader()

documents = pdf_loader.load_pdf("./data/pdfs/employee_handbook.pdf")

chunks = split_documents(documents)

print(f"Documents: {len(documents)}")
print(f"Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print("-" * 50)
    print(chunk.page_content[:150])