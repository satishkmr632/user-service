import databases
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from src.user_service.core.database import engine
from src.user_service.models import user
from src.user_service.api.v1 import users
from src.user_service.core.config import settings

database = databases.Database(settings.database_url)
app = FastAPI(title="User Service")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.include_router(users.router)

@app.on_event("startup")
async def on_startup():
    await database.connect()

@app.on_event("shutdown")
async def on_startup():
    await database.disconnect()
