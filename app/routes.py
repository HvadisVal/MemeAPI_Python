from fastapi import APIRouter, HTTPException, Depends
from app.database import memes_collection
from app.models import Meme
from bson import ObjectId
import asyncio

router = APIRouter()

# Get All Memes
@router.get("/memes")
async def get_memes():
    memes = []
    async for meme in memes_collection.find():
        memes.append({**meme, "_id": str(meme["_id"])})
    return memes

# Add a New Meme
@router.post("/memes")
async def add_meme(meme: Meme):
    new_meme = await memes_collection.insert_one(meme.dict())
    return {"message": "Meme added!", "id": str(new_meme.inserted_id)}

# Vote for a Meme
@router.post("/memes/{meme_id}/vote")
async def vote_meme(meme_id: str, user_id: str):
    meme = await memes_collection.find_one({"_id": ObjectId(meme_id)})
    if not meme:
        raise HTTPException(status_code=404, detail="Meme not found")

    if user_id in meme["votedUsers"]:
        raise HTTPException(status_code=400, detail="User already voted")

    await memes_collection.update_one(
        {"_id": ObjectId(meme_id)},
        {"$inc": {"votes": 1}, "$push": {"votedUsers": user_id}}
    )

    return {"message": "Vote counted!"}

# Delete a Meme
@router.delete("/memes/{meme_id}")
async def delete_meme(meme_id: str):
    result = await memes_collection.delete_one({"_id": ObjectId(meme_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Meme not found")
    return {"message": "Meme deleted successfully"}
