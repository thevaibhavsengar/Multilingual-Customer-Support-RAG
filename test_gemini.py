from dotenv import load_dotenv

from rag.llm import get_llm

load_dotenv()

llm = get_llm()

response = llm.invoke(
    "What is the capital of India?"
)

print(response.content)