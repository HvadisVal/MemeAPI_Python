from fastapi import FastAPI
from app.routes import router as meme_router
from app.auth import router as auth_router

app = FastAPI()

app.include_router(meme_router, prefix="/api/memes")  
app.include_router(auth_router, prefix="/api/auth")   

@app.get("/")
def home():
    return {"message": "Meme Battle API is running!"}
