from sqlalchemy import Column, Integer, String
from src.user_service.db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)

