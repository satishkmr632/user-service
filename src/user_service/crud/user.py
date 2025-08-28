from sqlalchemy.orm import Session
from src.user_service.models.user import User, UserInDB
from src.user_service.schemas.user import UserCreate

def create_user(db: Session, user: UserCreate) -> User:
    from src.user_service.core.security import get_password_hash
    username = user.username
    email = user.email
    password = user.password
    password_hash = get_password_hash(password)
    db_user = UserInDB(username=username, email=email, hashed_password=password_hash)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str) -> User | None :
    user = db.query(UserInDB).filter(User.email==email).scalar()
    return  user