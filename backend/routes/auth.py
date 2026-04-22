from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from models.schemas import UserCreate, UserOut, Token
from core.security import (
    create_access_token,
    verify_password,
    get_password_hash,
    get_current_user
)
from services.db_service import create_user, get_user_by_username
from loguru import logger

router = APIRouter()


# =========================
# REGISTER
# =========================
@router.post("/register", response_model=UserOut)
async def register(user: UserCreate):
    existing_user = await get_user_by_username(user.username)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )

    hashed_password = get_password_hash(user.password)

    user_obj = await create_user(
        username=user.username,
        password=hashed_password
    )

    logger.info(f"User registered: {user.username}")

    return user_obj


# =========================
# LOGIN (OAuth2 FORM - CORRECT)
# =========================
@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db_user = await get_user_by_username(form_data.username)

    if not db_user or not verify_password(form_data.password, db_user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        data={"sub": db_user["username"]}
    )

    logger.info(f"User logged in: {form_data.username}")

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# =========================
# GET CURRENT USER
# =========================
@router.get("/me")
async def get_me(current_user=Depends(get_current_user)):
    return {
        "username": current_user["username"]
    }