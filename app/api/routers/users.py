from typing import List
from fastapi import APIRouter, HTTPException
from app.schemas.users import User

router = APIRouter()

users: List[User] = [
	User(id=1, username="john_doe", email="john@example.com"),
	User(id=2, username="jane_doe", email="jane@example.com")
]

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
	user = next((user for user in users if user.id == user_id), None)
	if not user:
		raise HTTPException(status_code=404, detail="User Not Found")
	return user
	