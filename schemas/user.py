from pydantic import BaseModel


class UserResponse(BaseModel):
    username: str
    role: str
    is_active: bool
