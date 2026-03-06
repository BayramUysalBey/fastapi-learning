from typing import List, Dict
from fastapi import FastAPI
from app.api.api import api_router
from app.core.settings import settings, Settings

app = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG_MODE)


app.include_router(api_router, prefix="/api/v1")

def calculate_total(price: float, quantity: int) -> float:
    return float(price * quantity)

def print_db_url(config: Settings):
    print(f"DATABASE_URL: {config.DATABASE_URL}")

print_db_url(settings)

def greet(name: str = "Guest") -> str:
    return f"Hello {name}! How are you today?"

user_scores: Dict[str, List[int]] = {
    "Alice": [85, 92, 78],
    "Boby": [95, 88, 91],
    "Charlize": [100, 100, 99]
}

@app.get("/")
async def root():
    return {"message": greet(), "project": settings.PROJECT_NAME}
