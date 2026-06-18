from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

class Message(BaseModel):
    text: str

@app.get("/")
def home():
    return {
        "status": "running",
        "service": "backend-api"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.post("/predict")
def predict(message: Message):
    return {
        "input": message.text,
        "response": f"Processed: {message.text}"
    }

@app.get("/config")
def config():
    return {
        "environment": os.getenv("ENVIRONMENT", "development")
    }
