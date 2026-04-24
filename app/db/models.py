from  sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float, Boolean, ForeignKey
from app.db.base import Base
import uuid


class User(Base):
	__tablename__ = "users"
	id: Mapped[uuid.UUID] = mapped_column(
		primary_key=True,
		default=uuid.uuid4,
		index=True
	)
	username: Mapped[str] = mapped_column(String(255))
	email: Mapped[str] = mapped_column(String(255), server_default="unknown@example.com")

class Item(Base):
	__tablename__ = "items"
	id: Mapped[uuid.UUID] = mapped_column(
		primary_key=True,
		default=uuid.uuid4,
		index=True
	)
	name: Mapped[str] = mapped_column(String(255), unique=True, index=True)
	price: Mapped[float] = mapped_column(Float())
	is_offer: Mapped[bool] = mapped_column(Boolean(), default=False, server_default="false")
	category: Mapped[str] = mapped_column(String(255))
	user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), index=True)
