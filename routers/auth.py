from fastapi import APIRouter

from schemas.auth import LoginRequest, TokenResponse
from services.auth import login_user

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest):
    return login_user(data)
