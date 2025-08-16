from sqlalchemy.orm import Session
from src.user_service.models.user import User
from src.user_service.schemas.user import UserCreate

def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
