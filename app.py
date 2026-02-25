from typing import List, Dict
from fastapi import FastAPI, UploadFile, HTTPException
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

app = FastAPI()

items = ["severity", "disease", "solutions", "meds"]



class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

@app.post("/items/", status_code=201)
async def create_item(item: Item):
    return {**item.model_dump(), "id": 1}	# item.model_dump() converts a Pydantic model instance into a standard 
											# Python dictionary so that its data can be easily manipulated or returned as a JSON response.
class Settings(BaseSettings):

    API_KEY: str = ""
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/search")
async def searching(q: str, limit: int = 10):
    return {"q": q, "limit": limit}


@app.get("/users/{user_id}/items")
async def get_user_items(user_id: int, category: str):
    return {"user_id": user_id, "category": category}


@app.get("/items")
async def get_items():
    return items


@app.post("/upload/")
async def upload_file(file: UploadFile):
    return {"filename": file.filename, "content_type": file.content_type}


@app.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item index out of range")
    items.pop(item_id)
    return None


def calculate_total(price: float, quantity: int) -> float:
    return float(price * quantity)


def greet(name: str = "Guest") -> str:
    return f"Hello {name}! How are you today?"


def process_names(names: List[str]) -> str:
    return ",".join(names)


user_scores: Dict[str, List[int]] = {
    "Alice": [85, 92, 78],
    "Boby": [95, 88, 91],
    "Charlize": [100, 100, 99]
}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}

