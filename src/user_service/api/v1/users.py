from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.user_service.schemas.user import UserCreate, UserRead
from src.user_service.crud.user import create_user
from src.user_service.core.database import SessionLocal

router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        print("db called")
        yield db
    finally:
        print("finally called")
        db.close()

@router.get("/")
async def read_root() -> dict[str, str]:
    """
    Hello World
    """
    return {"Hello": "World.."}

@router.post("/", response_model=UserRead)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)
