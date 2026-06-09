from fastapi import FastAPI

from app.routes.auth_routes import router as auth_router

app = FastAPI(
    title="Multilingual Crop Disease Knowledge Chatbot"
)

app.include_router(
    auth_router,
    prefix="/api/auth",
    tags=["Authentication"]
)

@app.get("/")
async def root():
    return {
        "message": "Backend Running Successfully"
    }