import os

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS


FAISS_INDEX_PATH = "./faiss_index"


def get_embeddings():

    return GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001"
    )


def create_vector_store(chunks):

    print("\nCreating FAISS Index...")

    embeddings = get_embeddings()

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    os.makedirs(
        FAISS_INDEX_PATH,
        exist_ok=True
    )

    vector_store.save_local(
        FAISS_INDEX_PATH
    )

    print(
        "\nFAISS Index Created & Saved Successfully!"
    )

    return vector_store


def load_vector_store():

    print(
        "\nLoading Existing FAISS Index..."
    )

    embeddings = get_embeddings()

    vector_store = FAISS.load_local(
        FAISS_INDEX_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    print(
        "\nFAISS Index Loaded Successfully!"
    )

    return vector_store


def vector_store_exists():

    return os.path.exists(
        FAISS_INDEX_PATH
    )