from pydantic import BaseModel, EmailStr

class UserRegister(BaseModel):
    full_name: str
    mobile_number: str
    email: EmailStr
    password: str
    state: str
    district: str
    preferred_language: str
    role: str = "farmer"

class UserLogin(BaseModel):
    email: EmailStr
    password: str