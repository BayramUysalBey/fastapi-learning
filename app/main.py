from fastapi import FastAPI
from app.api.routers import status, items
from app.core.settings import settings

app = FastAPI(
    title="Testing Area",
    description="Testing Area for FastAPI",
    version="1.0.0"
)

app.include_router(status.router)
app.include_router(items.router)
