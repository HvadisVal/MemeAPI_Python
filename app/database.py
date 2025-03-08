from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://dbuser:<db_password>@cluster0.ouhi1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

client = AsyncIOMotorClient(MONGO_URI)
db = client["meme_battle_db"]  # Replace with your actual DB name
memes_collection = db["memes"]
users_collection = db["users"]
