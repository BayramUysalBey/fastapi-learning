from uuid import UUID
from pydantic import BaseModel, EmailStr
from typing import Optional

class Item(BaseModel):
    id: UUID
    name: str
    price: float
    is_offer: bool = False
    user_id: UUID
    category: str

class ItemCreate(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = False
    user_id: UUID
    category: str

class User(BaseModel):
    id: UUID
    username: str
    email: EmailStr

class FileUploadResponse(BaseModel):
    filename: str
    content_type: str
