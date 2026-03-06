from typing import List
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

items = ["severity", "disease", "solutions", "meds"]

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

@router.get("/")
async def get_items():
    return items

@router.get("/{item_id}")
async def read_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "name": items[item_id]}

@router.post("/", status_code=201)
async def create_item(item: Item):
    items.append(item.name)
    return {**item.model_dump(), "id": len(items) - 1}

@router.delete("/{item_id}", status_code=204)
async def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item index out of range")
    items.pop(item_id)
    return None
