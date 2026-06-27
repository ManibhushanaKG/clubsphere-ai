from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

client = QdrantClient(url="http://localhost:6333")

COLLECTION = "club_docs"

existing = [c.name for c in client.get_collections().collections]

if COLLECTION in existing:
    print("Deleting old collection...")
    client.delete_collection(COLLECTION)

print("Creating new collection...")

client.create_collection(
    collection_name=COLLECTION,
    vectors_config=VectorParams(
        size=3072,
        distance=Distance.COSINE
    )
)

print("✅ Collection created with vector size 3072.")