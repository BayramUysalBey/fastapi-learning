from typing import List, Optional
from fastapi import APIRouter, HTTPException, UploadFile
from app.schemas.items import Item, ItemCreate, User, FileUploadResponse
from app.schemas.search import SearchResult

router = APIRouter()

items: List[Item] = [
    Item(id=1, name="Foo", price=10.0, user_id=1, category="A"),
    Item(id=2, name="Bar", price=20.0, user_id=1, category="B"),
    Item(id=3, name="Baz", price=30.0, user_id=2, category="A")
]

users: List[User] = [
    User(id=1, username="alice"),
    User(id=2, username="bob")
]

@router.get("/items", response_model=List[Item])
async def get_items():
    return items

@router.post("/items", status_code=201, response_model=Item)
async def create_item(item_data: ItemCreate):
    new_id = max([i.id for i in items], default=0) + 1
    new_item = Item(id=new_id, **item_data.model_dump())
    items.append(new_item)
    return new_item

@router.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    item = next((i for i in items if i.id == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.get("/search", response_model=SearchResult)
async def searching(q: str, limit: int = 10):
    return SearchResult(q=q, limit=limit)

@router.post("/upload", response_model=FileUploadResponse)
async def upload_file(file: UploadFile):
    return FileUploadResponse(filename=file.filename, content_type=file.content_type)

@router.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: int):
    item_idx = next((idx for idx, i in enumerate(items) if i.id == item_id), None)
    if item_idx is None:
        raise HTTPException(status_code=404, detail="Item not found")
    items.pop(item_idx)
    return None

@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    user = next((u for u in users if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users/{user_id}/items", response_model=List[Item])
async def get_user_items(user_id: int, category: Optional[str] = None):
    results = [i for i in items if i.user_id == user_id]
    if category:
        results = [i for i in results if i.category == category]
    return results
