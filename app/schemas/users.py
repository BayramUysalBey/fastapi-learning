from pydantic import BaseModel,EmailStr

class UserBase(BaseModel):
	username: str
	email: EmailStr # email-validator package feature

class UserCreate(UserBase):
	password: str

class User(UserBase):
	id: int
	is_active: bool = True
