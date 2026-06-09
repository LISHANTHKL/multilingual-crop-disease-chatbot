from fastapi import FastAPI
from app.database.database import db

app = FastAPI()

@app.get("/")
async def root():

    collections = await db.list_collection_names()

    return {
        "message": "Backend Running",
        "collections": collections
    }