from chat import answer
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import SessionLocal
from models import User
from auth import hash_password, verify_password
from sqlalchemy import select

app= FastAPI()

class chat(BaseModel):
    question:str


class UserCreate(BaseModel):
    email: str
    password: str

@app.get("/")
def home():
    return{
        "message":"app is running"
    }

#@app.post("/chat")
async def chat(request:chat):
    result=await answer(request.question)
    return {
        "answer":result
    }
    

@app.post("/register")
def register(request: UserCreate):

    db = SessionLocal()

    hashed_password = hash_password(request.password)

    user = User(
        email=request.email,
        password_hash=hashed_password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    db.close()

    return {
        "message": "User created",
        "user_id": user.id
    }

@app.post("/login")
def login(request: UserCreate):

    db = SessionLocal()

    result = db.execute(
        select(User).where(User.email == request.email)
    )

    user = result.scalar_one_or_none()

    if not user:
        db.close()
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(
        request.password,
        user.password_hash
    ):
        db.close()
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    db.close()

    return {
        "message": "Login successful",
        "user_id": user.id
    }