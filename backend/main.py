import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ollama import Client

from api.ai_handler import Therapist


app = FastAPI()# Allow frontend to access the backend

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Client changes depending on deployment
client = Client(
    host=os.getenv("OLLAMA_HOST", "http://localhost:11434"),
)

# Useful for testing different model behavior
model = os.getenv("OLLAMA_MODEL", "mistral")

# Create the therapist
anne = Therapist("Anne Alysis", 32, model, client)

# TODO: Add support for other therapists

@app.get("/intro")
async def intro():
    """
    Generate a simple introduction of the therapist
    """

    introduction = "Provide a simple introduction of yourself"

    # She introduces herself
    return await anne.chat(introduction)

@app.post("/chat")
async def chat(request: dict):
    message = request.get("message", "")
    print(message)
    return await anne.chat(message)
