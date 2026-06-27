from google import genai
from qdrant_client import QdrantClient
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)
qdrant = QdrantClient(url="http://localhost:6333")

COLLECTION = "club_docs"


def embed(text: str):
    response = client.models.embed_content(
        model="models/gemini-embedding-001",
        contents=text
    )
    return response.embeddings[0].values


query = "Who is the president?"

query_vector = embed(query)

results = qdrant.query_points(
    collection_name=COLLECTION,
    query=query_vector,
    limit=3
)

print("\nTop Results:\n")

for point in results.points:
    print("=" * 60)
    print(point.payload["text"])
    print("=" * 60)