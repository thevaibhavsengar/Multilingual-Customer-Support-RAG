from langchain_community.document_loaders import PyPDFLoader

class PDFLoader:
    """
    Loads PDF documents using LangChain.
    """

    def __init__(self):
        print("PDF Loader initialized.")

    def load_pdf(self, pdf_path: str):
        """
        Loads a PDF and returns a list of Document objects.

        Parameters:
            pdf_path (str): Path to the PDF.

        Returns:
            list[Document]
        """

        try:

            loader = PyPDFLoader(pdf_path)

            documents = loader.load()

            print(f"\nSuccessfully loaded {len(documents)} pages.\n")

            return documents

        except Exception as e:

            print("Error loading PDF")

            print(e)

            return []