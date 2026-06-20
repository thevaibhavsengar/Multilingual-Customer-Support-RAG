from rag.retriever import get_retriever
from rag.llm import get_llm
from rag.memory import ConversationMemory


class RAGChain:

    def __init__(self, vector_store):

        self.retriever = get_retriever(vector_store)

        self.llm = get_llm()

        self.memory = ConversationMemory()

    def ask(self, question):

        docs = self.retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content for doc in docs
        )

        chat_history = self.memory.get_history()

        prompt = f"""
You are a helpful customer support assistant.

Conversation History:
{chat_history}

Context:
{context}

Question:
{question}

Answer using ONLY the provided context.
"""

        response = self.llm.invoke(prompt)

        answer = response.content

        self.memory.add_user_message(question)

        self.memory.add_ai_message(answer)

        return {
            "answer": answer,
            "sources": docs
        }