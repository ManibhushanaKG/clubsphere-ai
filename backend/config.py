from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

QDRANT_URL=os.getenv("https://1437e50a-ee00-4ba8-842c-5d21ab99686e.eu-west-1-0.aws.cloud.qdrant.io")

QDRANT_API_KEY=os.getenv("QDRANT_API_KEY")