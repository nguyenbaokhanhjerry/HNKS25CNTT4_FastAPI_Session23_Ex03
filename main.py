import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from middleware import request_logging_middleware
from routers.auth import router as auth_router
from routers.resources import router as resource_router
from routers.users import router as user_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

app = FastAPI(
    title="Learning Resource Management API",
    version="1.0.0",
    description="API quản lý tài nguyên học tập có JWT Authentication và Authorization",
)

# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type"],
)

# ============================================================
# Middleware
# ============================================================

app.middleware("http")(request_logging_middleware)

# ============================================================
# Routers
# ============================================================

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(resource_router)


@app.get("/health", tags=["Health"])
def health():
    return {
        "status": "ok",
        "service": "learning-resource-api",
    }
