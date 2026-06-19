from rag.retriever import get_retriever
from rag.llm import get_llm


class RAGChain:
    def __init__(self, vector_store):

        self.retriever = get_retriever(vector_store)

        self.llm = get_llm()

    def ask(self, question: str):

        docs = self.retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content for doc in docs
        )

        prompt = f"""
Answer the question using ONLY the context below.

Context:
{context}

Question:
{question}
"""

        response = self.llm.invoke(prompt)

        return {
            "answer": response.content,
            "sources": docs
        }