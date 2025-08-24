import databases
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.user_service.core.config import settings

database = databases.Database(settings.database_url)

engine = create_engine(settings.database_url, future=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
