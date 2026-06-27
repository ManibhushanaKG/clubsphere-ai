# ClubSphere AI

ClubSphere AI is an AI-powered **Club & Community Intelligence Agent** that enables users to upload club or community documents and interact with them using natural language. The system leverages **Retrieval-Augmented Generation (RAG)** with **Gemini AI** and **Qdrant** to provide accurate, context-aware answers grounded in uploaded documents.

---

## Features

* Upload PDF documents
* Automatic PDF text extraction
* Intelligent document chunking
* Gemini Embeddings for semantic search
* Qdrant Vector Database
* AI-powered Question Answering
* Conversation Memory
* Source Citation
* Document Summarization
* Recommendation generation based on document context

---

## Tech Stack

### Frontend

* React (Vite)

### Backend

* FastAPI
* Python

### AI

* Gemini 2.5 Flash
* Gemini Embedding API

### Database

* Qdrant Vector Database

### Other Tools

* Docker
* PyPDF

---

## Project Structure

```
clubsphere-ai/
│
├── backend/
│   ├── main.py
│   ├── upload.py
│   ├── memory.py
│   ├── config.py
│   ├── requirements.txt
│   ├── .env
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

## Prerequisites

Install the following before running the project:

* Python 3.11+
* Node.js (v18 or later)
* Docker Desktop
* Git

---

## Environment Variables

Create a file named `.env` inside the **backend** folder.

Example:

```
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

QDRANT_URL=http://localhost:6333

QDRANT_API_KEY=
```

Get your Gemini API key from:

https://aistudio.google.com/app/apikey

---

## Backend Setup

Navigate to the backend folder.

```
cd backend
```

Create a virtual environment.

```
python -m venv venv
```

Activate it.

Windows

```
venv\Scripts\activate
```

Install dependencies.

```
pip install -r requirements.txt
```

Start the FastAPI server.

```
uvicorn main:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

---

## Frontend Setup

Open another terminal.

```
cd frontend
```

Install packages.

```
npm install
```

Run the React application.

```
npm run dev
```

Frontend runs on:

```
http://localhost:5173
```

---

## Qdrant Setup (Docker)

Pull and run Qdrant.

```
docker run -d --name qdrant -p 6333:6333 qdrant/qdrant
```

If the container already exists:

```
docker start qdrant
```

Qdrant Dashboard:

```
http://localhost:6333/dashboard
```

---

## How to Use

1. Start Docker Desktop.
2. Start the Qdrant container.
3. Start the FastAPI backend.
4. Start the React frontend.
5. Open `http://localhost:5173`.
6. Upload a PDF document.
7. Ask questions in natural language.
8. View AI-generated answers with source citations.

---

## Example Questions

* Who is the President of the club?
* What are the responsibilities of the Treasurer?
* List all major events.
* Who participated in the AI Workshop?
* Summarize the club.
* Who should lead the next AI Workshop?

---

## Architecture

```
                 User
                   │
                   ▼
          React Frontend
                   │
                   ▼
           FastAPI Backend
                   │
        ┌──────────┴──────────┐
        │                     │
        ▼                     ▼
 Conversation Memory     Gemini Embeddings
        │                     │
        └──────────┬──────────┘
                   ▼
              Qdrant Search
                   │
                   ▼
          Retrieved Context
                   │
                   ▼
          Gemini 2.5 Flash
                   │
                   ▼
      Response + Source Citation
```

---

## Future Improvements

* Multi-document retrieval
* Voice interaction
* Authentication
* Role-based access
* Cloud deployment
* Multi-agent architecture using Google ADK/Lyzr

---

## Author

**Manibhushana KG**

B.E Computer Science Engineering

Bangalore Institute of Technology
