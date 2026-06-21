from rag.loader import PDFLoader

# Create loader object
loader = PDFLoader()

# Load PDF
documents = loader.load_pdf("data/pdfs/employee_handbook.pdf")

print("=" * 50)
print("Total Pages:", len(documents))
print("=" * 50)

for i, doc in enumerate(documents):
    print(f"\nPage {i+1}")
    print("-" * 50)
    print(doc.page_content)
    print("\nMetadata:")
    print(doc.metadata)