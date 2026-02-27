from fastapi import FastAPI
from app.api.routers import status, items
from app.core.settings import settings

app = FastAPI(
    title="Dementia Tracker V1 API",
    description="A modular FastAPI application for Dementia Tracker V1.",
    version="1.0.0"
)

# Include Routers
app.include_router(status.router)
app.include_router(items.router)
