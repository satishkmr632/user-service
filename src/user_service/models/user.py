from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.user_service.db.session import Base
from src.user_service.models.roles import user_roles

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String, nullable=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)

    profile: Mapped["UserProfile"] = relationship("UserProfile", uselist=False, back_populates="user", cascade="all, delete")
    roles: Mapped["Role"] = relationship("Role", secondary=user_roles, back_populates="users")

class UserInDB(User):
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)

