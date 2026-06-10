from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Authentication
from app.routes.auth_routes import router as auth_router

# Dashboard
from app.routes.dashboard_routes import router as dashboard_router

# Weather
from app.routes.weather_routes import router as weather_router

# Profile
from app.routes.profile_routes import router as profile_router

# Chat
from app.routes.chat_routes import router as chat_router

# Intent Classification
from app.routes.intent_routes import router as intent_router

# Entity Recognition
from app.routes.entity_routes import router as entity_router

#disease
from app.routes.disease_routes import (
    router as disease_router
)
#rag
from app.routes.rag_routes import (
    router as rag_router
)
#mutilaung
from app.routes.multilingual_routes import (
    router as multilingual_router
)
#weather
from app.routes.recommendation_routes import (
    router as recommendation_router
)
#chatbot
from app.routes.chatbot_routes import (
    router as chatbot_router
)
#voice
from app.routes.voice_routes import (
    router as voice_router
)

app = FastAPI(
    title="Multilingual Crop Disease Knowledge Chatbot",
    description="AI-powered Agriculture Assistant using NLP, Deep Learning, FastAPI, React, and MongoDB",
    version="1.0.0"
)

# =========================
# CORS
# =========================
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

# =========================
# Authentication
# =========================
app.include_router(
    auth_router,
    prefix="/api/auth",
    tags=["Authentication"]
)

# =========================
# Dashboard
# =========================
app.include_router(
    dashboard_router,
    prefix="/api/dashboard",
    tags=["Dashboard"]
)

# =========================
# Weather
# =========================
app.include_router(
    weather_router,
    prefix="/api/weather",
    tags=["Weather"]
)

# =========================
# Profile
# =========================
app.include_router(
    profile_router,
    prefix="/api/profile",
    tags=["Profile"]
)

# =========================
# Chat
# =========================
app.include_router(
    chat_router,
    prefix="/api/chat",
    tags=["Chat"]
)

# =========================
# Intent Classification
# =========================
app.include_router(
    intent_router,
    prefix="/api/intent",
    tags=["Intent Classification"]
)

# =========================
# Entity Recognition
# =========================
app.include_router(
    entity_router,
    prefix="/api/entity",
    tags=["Entity Recognition"]
)
#disease
app.include_router(
    disease_router,
    prefix="/api/disease",
    tags=["Disease Recognition"]
)
#rag
app.include_router(
    rag_router,
    prefix="/api/rag",
    tags=["RAG Search"]
)
#multilang
app.include_router(
    multilingual_router,
    prefix="/api/multilingual",
    tags=["Multilingual NLP"]
)
#weather
app.include_router(
    recommendation_router,
    prefix="/api/recommendation",
    tags=["Recommendation Engine"]
)
#chatbot
app.include_router(
    chatbot_router,
    prefix="/api/chatbot",
    tags=["AI Agriculture Assistant"]
)
#voice
app.include_router(
    voice_router,
    prefix="/api/voice",
    tags=["Voice AI"]
)

# =========================
# Root Endpoint
# =========================
@app.get("/", tags=["Root"])
async def root():
    return {
        "status": "success",
        "message": "Backend Running Successfully",
        "project": "Multilingual Crop Disease Knowledge Chatbot",
        "version": "1.0.0"
    }