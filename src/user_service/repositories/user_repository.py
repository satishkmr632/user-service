from sqlalchemy.orm import Session
from src.user_service.models.user import User, UserInDB
from src.user_service.models.user_profile import UserProfile

class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, user_id: int) -> User:
        return self.db.query(UserInDB).filter(UserInDB.id==user_id).first()
    
    def get_by_email(self, email: str) -> User:
        return self.db.query(UserInDB).filter(UserInDB.email==email).first()
    
    def create(self, username: str, email: str, password: str) -> User:
        user = UserInDB(username=username, email=email, hashed_password=password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def create_profile(self, user_id, first_name, last_name) -> UserProfile:
        user_profile = UserProfile(first_name=first_name, last_name=last_name)
        self.db.add(user_profile)
        self.db.commit()
        self.db.refresh(user_profile)
        return user_profile