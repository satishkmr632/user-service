from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Annotated
from src.user_service.schemas.user import UserCreate, UserRead
from src.user_service.crud.user import create_user
from src.user_service.core.database import SessionLocal

from src.user_service.core.security import oauth2_scheme

router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        print("db called")
        yield db
    finally:
        print("finally called")
        db.close()

# @router.get("/")
# async def read_root() -> dict[str, str]:
#     """
#     Hello World
#     """
#     return {"Hello": "World..1"}

@router.post("/", response_model=UserRead)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/item/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]) -> dict:
    return {"token": token}