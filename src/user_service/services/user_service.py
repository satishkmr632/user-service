from passlib.context import CryptContext
from src.user_service.repositories.user_repository import UserRepository
from src.user_service.models.user import User
from src.user_service.core.security import get_password_hash, verify_password

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:

    def __init__(self, db):
        self.repo = UserRepository(db)

    def get_user(self, user_id: int) -> User | None:
        return self.repo.get_by_id(user_id)
    
    def get_user_by_email(self, email: str) -> User:
        return self.repo.get_by_email(email)

    def register_user(self, username: str, email: str, password: str) -> User:
        password = get_password_hash(password)
        return self.repo.create(username, email, password)

    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)
    
    def authenticate_user(self, email, password):
        user = self.repo.get_by_email(email)
        is_password_verified = verify_password(password, user.hashed_password)
        if user and is_password_verified:
            return user
        return False
    
    def add_profile(self, user_id: int, first_name, last_name):
        return self.repo.create_profile(user_id, first_name, last_name)
    
