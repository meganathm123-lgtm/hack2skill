from fastapi import APIRouter, HTTPException, status, Depends
from models.schemas import UserCreate, UserOut, Token, UserLogin
from core.security import (
    create_access_token, verify_password, get_password_hash, get_current_user
)
from services.db_service import create_user, get_user_by_username
from loguru import logger

router = APIRouter()

@router.post("/register", response_model=UserOut)
async def register(user: UserCreate):
    if await get_user_by_username(user.username):
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_pw = get_password_hash(user.password)
    user_obj = await create_user(user.username, hashed_pw)
    logger.info(f"User registered: {user.username}")
    return user_obj

@router.post("/login", response_model=Token)
async def login(user: UserLogin):
    db_user = await get_user_by_username(user.username)
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token({"sub": db_user["username"]})
    logger.info(f"User logged in: {user.username}")
    return {"access_token": access_token, "token_type": "bearer"}
