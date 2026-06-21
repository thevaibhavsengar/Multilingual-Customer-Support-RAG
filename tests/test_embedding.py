from dotenv import load_dotenv
from rag.embeddings import get_embedding_model

load_dotenv()

embeddings = get_embedding_model()

vector = embeddings.embed_query(
    "Employees get 20 paid leaves every year."
)

print(len(vector))
print(vector[:10])