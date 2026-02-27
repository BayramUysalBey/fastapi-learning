from pydantic import BaseModel
from typing import List, Optional

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

class ItemCreate(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = False

class User(BaseModel):
    user_id: int
