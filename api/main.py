import os

from fastapi import (
    FastAPI,
    UploadFile,
    File
)

from dotenv import load_dotenv

from rag.loader import PDFLoader
from rag.splitter import split_documents
from rag.vectorstore import (
    create_vector_store,
    load_vector_store,
    vector_store_exists
)
from rag.chain import RAGChain

from api.schemas import (
    QueryRequest,
    QueryResponse,
    UploadResponse
)

load_dotenv()

app = FastAPI(
    title="Customer Support RAG API"
)

# Global RAG Chain
rag_chain = None

# Load existing FAISS index on startup
if vector_store_exists():

    print("\nFound existing FAISS index.")

    vector_store = load_vector_store()

    rag_chain = RAGChain(
        vector_store
    )

    print(
        "\nRAG Chain initialized from saved index."
    )


@app.get("/")
def root():

    return {
        "message": "RAG API Running"
    }


@app.post(
    "/upload",
    response_model=UploadResponse
)
async def upload_pdf(
    file: UploadFile = File(...)
):

    global rag_chain

    os.makedirs(
        "./data/uploads",
        exist_ok=True
    )

    file_path = (
        f"./data/uploads/{file.filename}"
    )

    with open(
        file_path,
        "wb"
    ) as f:

        f.write(
            await file.read()
        )

    print(
        f"\nUploaded: {file.filename}"
    )

    loader = PDFLoader()

    documents = loader.load_pdf(
        file_path
    )

    chunks = split_documents(
        documents
    )

    vector_store = create_vector_store(
        chunks
    )

    rag_chain = RAGChain(
        vector_store
    )

    return UploadResponse(
        message=f"{file.filename} uploaded successfully"
    )


@app.post(
    "/query",
    response_model=QueryResponse
)
def query_rag(
    request: QueryRequest
):

    global rag_chain

    if rag_chain is None:

        return QueryResponse(
            answer="Please upload a PDF first.",
            sources=[]
        )

    result = rag_chain.ask(
        request.question
    )

    sources = []

    for doc in result["sources"]:

        page = (
            doc.metadata.get(
                "page",
                0
            ) + 1
        )

        filename = os.path.basename(
            doc.metadata.get(
                "source",
                "Unknown"
            )
        )

        source_text = (
            f"{filename} (Page {page})"
        )

        if source_text not in sources:
            sources.append(
                source_text
            )

    return QueryResponse(
        answer=result["answer"],
        sources=sources
    )