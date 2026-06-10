from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext

from app.models.user_model import (
    UserRegister,
    UserLogin
)

from app.database.database import db

from app.auth.auth_handler import create_access_token

router = APIRouter()

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    deprecated="auto"
)

@router.post("/register")
async def register(user: UserRegister):

    existing_user = await db.users.find_one(
        {"email": user.email}
    )

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    hashed_password = pwd_context.hash(
        user.password
    )

    user_data = user.dict()

    user_data["password"] = hashed_password

    await db.users.insert_one(user_data)

    return {
        "message": "User registered successfully"
    }


@router.post("/login")
async def login(user: UserLogin):

    existing_user = await db.users.find_one(
        {"email": user.email}
    )

    if not existing_user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    valid_password = pwd_context.verify(
        user.password,
        existing_user["password"]
    )

    if not valid_password:

        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    token = create_access_token(
        {
            "email": existing_user["email"],
            "role": existing_user["role"]
        }
    )

    return {
        "access_token": token,
        "role": existing_user["role"]
    }