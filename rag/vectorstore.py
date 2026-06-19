from langchain_community.vectorstores import FAISS

from rag.embeddings import get_embedding_model


def create_vector_store(chunks):
    """
    Create a FAISS vector store from chunks.
    """

    embeddings = get_embedding_model()

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vector_store