from fastapi import APIRouter, HTTPException, Depends
from app.database import users_collection
from app.models import User
from passlib.context import CryptContext
from jose import jwt
from pydantic import BaseModel
import os

router = APIRouter()

SECRET_KEY = "your_secret_key"  # Change this
ALGORITHM = "HS256"

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Pydantic models for request validation
class LoginRequest(BaseModel):
    email: str
    password: str

# Register a User
@router.post("/register")
async def register_user(user: User):
    existing_user = await users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    hashed_password = pwd_context.hash(user.password)
    user_dict = user.dict()
    user_dict["password"] = hashed_password

    new_user = await users_collection.insert_one(user_dict)
    return {"message": "User registered!", "id": str(new_user.inserted_id)}

# Login a User
@router.post("/login")
async def login_user(login_data: LoginRequest):
    user = await users_collection.find_one({"email": login_data.email})
    if not user or not pwd_context.verify(login_data.password, user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = jwt.encode({"email": user["email"]}, SECRET_KEY, algorithm=ALGORITHM)
    return {"message": "Login successful!", "token": token}
