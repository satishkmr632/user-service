from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Annotated
from src.user_service.schemas.user import UserCreate, UserRead, Token
from src.user_service.db.session import get_db
from src.user_service.core.security import create_access_token
from src.user_service.schemas.user import LoginRequest
from src.user_service.services.user_service import UserService


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register_user(request_data: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService(db)
    user = user_service.get_user_by_email(request_data.email)
    if user:
        return HTTPException(status_code=400, details="Email Already Registered.")
    user = user_service.register_user(request_data.username, request_data.email, request_data.password)
    return {"message": "User Created Successfully", "user_id": user.id}


@router.post("/login")
def login_user(request_data: LoginRequest, db: Session = Depends(get_db)):
    user_service = UserService(db)
    user = user_service.authenticate_user(request_data.email, request_data.password)
    if user:
        access_token = create_access_token(data={"sub": user.email})
        return Token(access_token=access_token, token_type="bearer")
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
