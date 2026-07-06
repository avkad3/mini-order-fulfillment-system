from enum import Enum

from sqlalchemy import Enum as SqlEnum, ForeignKey, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class POLineStatus(str, Enum):
    VALID = "Valid"
    INVALID = "Invalid"
    APPROVED = "Approved"
    PARTIAL = "Partial"
    REJECTED = "Rejected"


class PurchaseOrderItem(Base):
    __tablename__ = "purchase_order_items"

    id: Mapped[int] = mapped_column(primary_key=True)

    purchase_order_id: Mapped[int] = mapped_column(
        ForeignKey("purchase_orders.id"),
        nullable=False,
    )

    material_id: Mapped[int] = mapped_column(
        ForeignKey("materials.id"),
        nullable=False,
    )

    ordered_quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    approved_quantity: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    unit_price: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    status: Mapped[POLineStatus] = mapped_column(
        SqlEnum(POLineStatus),
        default=POLineStatus.VALID,
    )

    purchase_order = relationship(
        "PurchaseOrder",
        back_populates="items",
    )

    material = relationship("Material")