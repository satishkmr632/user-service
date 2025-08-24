from sqlalchemy import Column, String, Integer, Table, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.user_service.db.session import Base


user_roles= Table(
    "user_roles",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("role_id", ForeignKey("roles.id"), primary_key=True)
)

class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)

    users = relationship('User', secondary=user_roles, back_populates='roles')