from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin


class Inventory(Base, TimestampMixin):
    __tablename__ = "inventory"

    id: Mapped[int] = mapped_column(primary_key=True)

    material_id: Mapped[int] = mapped_column(
        ForeignKey("materials.id"),
        unique=True,
    )

    available_quantity: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    reserved_quantity: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    material = relationship("Material")