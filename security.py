import os
from datetime import datetime, timedelta, timezone

from jose import jwt

SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret-key-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_minutes: int = ACCESS_TOKEN_EXPIRE_MINUTES) -> str:
    payload = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
    payload["exp"] = expire

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
