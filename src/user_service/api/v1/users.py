from fastapi import APIRouter, Depends
from src.user_service.schemas.user import UserCreate, UserRead
from src.user_service.models.user import User
from src.user_service.core.dependencies import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/protected")
async def read_root(current_user: User = Depends(get_current_user)) -> dict[str, str]:
    """
    Hello World
    """
    return {"Hello": "World..2"}
