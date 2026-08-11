from chat import answer
from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

class chat(BaseModel):
    question:str

@app.get("/")
def home():
    return{
        "message":"app is running"
    }

@app.post("/chat")
def chat(request:chat):
    result=answer(request.question)
    return {
        "answer":result
    }
    

