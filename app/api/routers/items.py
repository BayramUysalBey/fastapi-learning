from typing import List, Optional, Dict
from fastapi import APIRouter, HTTPException, UploadFile
from app.schemas.items import Item, ItemCreate

router = APIRouter()

items = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@router.get("/items", response_model=List[dict])
async def get_items():
    return items

@router.post("/items/", status_code=201)
async def create_item(item: Item):
    return item

@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@router.get("/search")
async def searching(q: str, limit: int = 10):
    return {"q": q, "limit": limit}

@router.post("/upload/")
async def upload_file(file: UploadFile):
    return {"filename": file.filename, "content_type": file.content_type}

@router.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item index out of range")
    items.pop(item_id)
    return None

@router.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}

@router.get("/users/{user_id}/items")
async def get_user_items(user_id: int, category: str):
    return {"user_id": user_id, "category": category}
