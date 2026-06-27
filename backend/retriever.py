from google import genai
from qdrant_client import QdrantClient
from config import GEMINI_API_KEY, QDRANT_URL, QDRANT_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

qdrant = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

COLLECTION = "club_docs"


def embed(text: str):
    response = client.models.embed_content(
        model="models/gemini-embedding-001",
        contents=text
    )
    return response.embeddings[0].values