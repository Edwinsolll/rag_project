from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "RAG API is running"
    }

@app.get("/")
def hom():
    return {
        "message": "RAG API is running"
    }


@app.post("/chat")
def chat(data: Question):

    return {
        "question": data.question,
        "answer": "This will eventually come from my RAG system."
    }