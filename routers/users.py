from fastapi import APIRouter, Depends

from auth import get_current_user
from schemas.user import UserResponse

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me", response_model=UserResponse)
def read_current_user(current_user: dict = Depends(get_current_user)):
    return current_user
