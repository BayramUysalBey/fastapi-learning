from fastapi import APIRouter
from app.api.routers import users, orders, items, status

api_router = APIRouter()

api_router.include_router(status.router, tags=["status"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(orders.router, prefix="/orders", tags=["orders"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
