from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class Meme(BaseModel):
    title: str
    imageUrl: str
    description: str
    creator: str  # User ID
    votes: int = 0
    votedUsers: List[str] = []
    createdAt: Optional[datetime] = datetime.utcnow()

class User(BaseModel):
    name: str
    email: str
    password: str
