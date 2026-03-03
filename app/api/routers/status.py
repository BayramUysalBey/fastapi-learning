from fastapi import APIRouter
from app.schemas.status import HealthStatus

router = APIRouter()

@router.get("/", response_model=dict)
async def main_home():
    return {"message": "Welcome to the Testing Area"}

@router.get("/health", response_model=HealthStatus)
async def health():
    return HealthStatus(status="up")
