from fastapi import FastAPI
from app.api.routers import items
from app.api.routers import status as status_router
from app.core.settings import settings
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import timedelta
from app.db.session import get_db
from app.db.models import User
from app.core.security import verify_password, create_access_token, get_current_user, get_password_hash
from pydantic import BaseModel
import uuid

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: str | uuid.UUID
    username: str
    email: str
    
    class Config:
        from_attributes = True

app = FastAPI(
    title="FastAPI Learning",
    description="Learning Project for FastAPI",
    version="1.0.0"
)


@app.get("/")
async def main():
    return {"message": "Welcome to the FastAPI Learning API!"}

@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
	user = await db.execute(select(User).where(User.username == form_data.username))
	user = user.scalar_one_or_none()
	if not user or not verify_password(form_data.password, user.hashed_password):
		raise HTTPException(
		status_code=status.HTTP_401_UNAUTHORIZED,
		detail="Incorrect username or password",
		headers={"WWW-Authenticate": "Bearer"},
		)
	access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
	access_token = create_access_token(
		data={"sub": user.username},
		expires_delta=access_token_expires
	)
	return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me",  response_model=UserResponse)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.post("/users/")
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

app.include_router(status_router.router)
app.include_router(items.router)