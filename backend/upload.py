import uuid
from io import BytesIO

from pypdf import PdfReader

from google import genai

from qdrant_client import QdrantClient
from qdrant_client.models import (
    PointStruct,
    VectorParams,
    Distance
)

from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

qdrant = QdrantClient(url="http://localhost:6333")

COLLECTION = "club_docs"


def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks


def embed(text):
    response = client.models.embed_content(
        model="models/gemini-embedding-001",
        contents=text
    )

    return response.embeddings[0].values


def ingest_pdf(file_bytes, filename):

    # Read PDF
    reader = PdfReader(BytesIO(file_bytes))

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"

    # Split into chunks
    chunks = chunk_text(text)

    points = []

    for chunk in chunks:

        vector = embed(chunk)

        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload={
                    "text": chunk,
                    "source": filename
                }
            )
        )

    # -------------------------------------------------
    # DELETE OLD COLLECTION (removes previous PDFs)
    # -------------------------------------------------
    collections = [c.name for c in qdrant.get_collections().collections]

    if COLLECTION in collections:
        qdrant.delete_collection(COLLECTION)

    # -------------------------------------------------
    # CREATE NEW COLLECTION
    # -------------------------------------------------
    qdrant.create_collection(
        collection_name=COLLECTION,
        vectors_config=VectorParams(
            size=3072,
            distance=Distance.COSINE
        )
    )

    # -------------------------------------------------
    # INSERT NEW PDF
    # -------------------------------------------------
    qdrant.upsert(
        collection_name=COLLECTION,
        points=points
    )

    return len(points)