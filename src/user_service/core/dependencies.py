import jwt
from fastapi import Depends, HTTPException, status
from jwt.exceptions import InvalidTokenError
from datetime import timedelta, datetime, timezone
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from src.user_service.services.user_service import UserService
from src.user_service.db.session import SessionLocal


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # We can use this when we need to authenticate user using email and password
security = HTTPBearer()

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception
    user_service = UserService(db)
    user = user_service.get_user_by_email(email)
    if user is None:
        raise credentials_exception
    return user