from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ChatLog(BaseModel):
    user_id: str
    query: str
    intent: Optional[str] = None
    crop: Optional[str] = None
    disease: Optional[str] = None
    response: str
    timestamp: datetime = datetime.utcnow()