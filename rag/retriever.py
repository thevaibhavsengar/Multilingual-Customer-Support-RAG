def get_retriever(vector_store):
    """
    Create a retriever from FAISS.
    """

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 1}
    )

    return retriever