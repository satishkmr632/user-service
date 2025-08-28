from fastapi import FastAPI
from src.user_service.db.session import database
from src.user_service.api.v1 import users, auth

app = FastAPI(title="User Service")

app.include_router(users.router)
app.include_router(auth.router)

@app.on_event("startup")
async def on_startup():
    await database.connect()

@app.on_event("shutdown")
async def on_startup():
    await database.disconnect()
