from fastapi import APIRouter, UploadFile, HTTPException
from app.core.settings import settings

router = APIRouter()

@router.get("/health")
async def health():
    return {"status": "ok", "project_name": settings.PROJECT_NAME}

@router.get("/search")
async def searching(q: str, limit: int = 10):
    return {"q": q, "limit": limit}

@router.post("/upload/")
async def upload_file(file: UploadFile):
    return {"filename": file.filename, "content_type": file.content_type}
