from typing import List
from fastapi import APIRouter, HTTPException, UploadFile
from app.schemas.orders import Orders

router = APIRouter()

orders: List[Orders] = [
	Orders(id=1, orders_name="Laptop", category="Big Screen"),
	Orders(id=2, orders_name="Phone", category="Small Screen")
]


@router.get("/{order_id}", response_model=Orders)
async def get_order(order_id: int):
	order = next((order for order in orders if order.id == order_id), None)
	if not order:
		raise HTTPException(status_code=404, detail="Order Not Found")
	return order