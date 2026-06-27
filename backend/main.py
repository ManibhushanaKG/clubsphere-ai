from retriever import embed, qdrant
from memory import conversation
from fastapi import UploadFile, File
from upload import ingest_pdf
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google import genai
from config import GEMINI_API_KEY

app = FastAPI(title="ClubSphere AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = genai.Client(api_key=GEMINI_API_KEY)

@app.get("/")
def root():
    return {"message": "ClubSphere AI Backend Running"}

@app.get("/health")
def health():
    return {"status": "ok"}



@app.get("/chat")
def chat(prompt: str):

    query_vector = embed(prompt)

    results = qdrant.query_points(
        collection_name="club_docs",
        query=query_vector,
        limit=3
    )

    context = ""
    sources = set()

    for point in results.points:
        context += point.payload["text"] + "\n\n"
        sources.add(point.payload["source"])

    history = ""

    for msg in conversation:
        history += f"{msg['role']}: {msg['text']}\n"

    final_prompt = f"""
You are ClubSphere AI.

Use the conversation history if needed.

Conversation History:

{history}

Relevant Club Documents:

{context}

Current User Question:

{prompt}

If the answer is not in the documents, reply:

"I couldn't find that information in the uploaded documents."
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=final_prompt
    )

    answer = response.text

    conversation.append({
        "role": "User",
        "text": prompt
    })

    conversation.append({
        "role": "Assistant",
        "text": answer
    })

    return {
    "reply": answer,
    "sources": list(sources)
    }   

@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    data = await file.read()

    count = ingest_pdf(data, file.filename)

    return {
        "message": "Upload successful",
        "chunks": count
    }