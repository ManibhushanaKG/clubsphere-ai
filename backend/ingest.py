import uuid
from google import genai
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
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


text = """
ClubSphere AI Club

President: Alice Johnson

Vice President: Bob Smith

AI Workshop:
Date: 15 July 2026

Venue:
Seminar Hall

Registration Fee:
Free
"""

vector = embed(text)

qdrant.upsert(
    collection_name=COLLECTION,
    points=[
        PointStruct(
            id=str(uuid.uuid4()),
            vector=vector,
            payload={
                "text": text,
                "source": "sample.txt"
            }
        )
    ]
)

print("Document stored successfully!")