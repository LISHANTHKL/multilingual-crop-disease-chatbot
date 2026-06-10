from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.auth_routes import router as auth_router
from app.routes.dashboard_routes import router as dashboard_router
from app.routes.weather_routes import router as weather_router
from app.routes.profile_routes import router as profile_router
from app.routes.chat_routes import router as chat_router

app = FastAPI(
    title="Multilingual Crop Disease Knowledge Chatbot",
    description="AI-powered Agriculture Assistant using NLP, Deep Learning, FastAPI, React, and MongoDB",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Authentication Routes
app.include_router(
    auth_router,
    prefix="/api/auth",
    tags=["Authentication"]
)

# Dashboard Routes
app.include_router(
    dashboard_router,
    prefix="/api/dashboard",
    tags=["Dashboard"]
)

# Weather Routes
app.include_router(
    weather_router,
    prefix="/api/weather",
    tags=["Weather"]
)

# Profile Routes
app.include_router(
    profile_router,
    prefix="/api/profile",
    tags=["Profile"]
)

# Chat Routes
app.include_router(
    chat_router,
    prefix="/api/chat",
    tags=["Chat"]
)

@app.get("/", tags=["Root"])
async def root():
    return {
        "status": "success",
        "message": "Backend Running Successfully",
        "project": "Multilingual Crop Disease Knowledge Chatbot",
        "version": "1.0.0"
    }

