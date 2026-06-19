from langchain_google_genai import GoogleGenerativeAIEmbeddings


def get_embedding_model():
    """
    Returns Gemini embedding model.
    """

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001"
    )

    return embeddings