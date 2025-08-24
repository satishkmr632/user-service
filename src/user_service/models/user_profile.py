import enum
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.user_service.db.session import Base

class GenderEnum(str, enum.Enum):
    MALE = "male"
    FEMALE = "female"
    Other = "other"

class UserProfile(Base):
    __tablename__ = "user_profiles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String, nullable=True)
    last_name: Mapped[str] = mapped(String, nullable=True)
    gender: Mapped[GenderEnum] = mapped_column(Enum(GenderEnum), nullable=True)

    user = relationship("User", uselist=False, back_populates="profile")