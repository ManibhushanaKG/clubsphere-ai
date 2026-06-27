# ClubSphere AI

ClubSphere AI is an AI-powered Club & Community Intelligence Agent that enables users to upload club or community documents and interact with them using natural language. The system leverages Retrieval-Augmented Generation (RAG), Google Gemini, and Qdrant Cloud to provide accurate, context-aware answers grounded in uploaded documents.

---

## Live Demo

Frontend (Vercel)

`https://clubsphere-ai.vercel.app`

Backend (Render)

`https://clubsphere-ai-backend.onrender.com`

---

## Features

* Upload PDF documents
* Automatic PDF text extraction
* Intelligent document chunking
* Semantic Search using Gemini Embeddings
* AI-powered Question Answering
* Conversation Memory
* Source Citation
* Document Summarization
* Recommendation generation based on document context
* Cloud deployment using Render and Vercel

---

## Tech Stack

### Frontend

* React
* Vite
* JavaScript

### Backend

* FastAPI
* Python

### AI

* Google Gemini 2.5 Flash
* Gemini Embedding API

### Vector Database

* Qdrant Cloud

### Deployment

* Render
* Vercel

---

## Project Structure

```
clubsphere-ai/
│
├── backend/
│   ├── main.py
│   ├── upload.py
│   ├── retriever.py
│   ├── memory.py
│   ├── config.py
│   ├── requirements.txt
│   └── ...
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── ...
│
├── README.md
└── .gitignore
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/ManibhushanaKG/clubsphere-ai.git

cd clubsphere-ai
```

---

## Backend Setup

```bash
cd backend

python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file inside the backend folder.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

QDRANT_URL=YOUR_QDRANT_CLOUD_URL

QDRANT_API_KEY=YOUR_QDRANT_API_KEY
```

Run the backend

```bash
uvicorn main:app --reload
```

Backend

```
http://127.0.0.1:8000
```

---

## Frontend Setup

```bash
cd frontend

npm install
```

Create a `.env` file inside the frontend folder.

```env
VITE_API_URL=http://127.0.0.1:8000
```

Run

```bash
npm run dev
```

Frontend

```
http://localhost:5173
```

---

## How It Works

1. User uploads a PDF document.
2. Text is extracted from the PDF.
3. The document is divided into semantic chunks.
4. Gemini Embeddings convert each chunk into vectors.
5. Embeddings are stored in Qdrant Cloud.
6. User asks a question.
7. The question is converted into an embedding.
8. Qdrant performs semantic search.
9. Relevant chunks are retrieved.
10. Gemini 2.5 Flash generates an answer using the retrieved context.
11. The response is returned with source citations.

---

## Example Questions

* Who is the President of the club?
* What are the responsibilities of the Treasurer?
* List all upcoming events.
* Summarize this document.
* What achievements are mentioned?
* Recommend improvements for future club events.

---

## System Architecture

```
                    User
                      │
                      ▼
             React + Vite Frontend
                      │
              HTTPS API Requests
                      │
                      ▼
               FastAPI Backend
                      │
       ┌──────────────┴──────────────┐
       ▼                             ▼
Conversation Memory          Gemini Embeddings
       │                             │
       └──────────────┬──────────────┘
                      ▼
               Qdrant Cloud
              Semantic Search
                      │
                      ▼
            Retrieved Context
                      │
                      ▼
            Gemini 2.5 Flash
                      │
                      ▼
      AI Response + Source Citation
```

---

## Future Improvements

* Multi-document retrieval
* Authentication
* Role-based access
* Voice interaction
* OCR support
* Image-based search
* Multi-agent workflow using Google ADK or Lyzr

---

## Author

Manibhushana KG

B.E. Computer Science Engineering

Bangalore Institute of Technology
