from pydantic import BaseModel

class Orders(BaseModel):
	id: int
	orders_name: str
	category: str