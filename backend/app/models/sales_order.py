from enum import Enum

from sqlalchemy import DateTime, Enum as SqlEnum, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin


class SalesOrderStatus(str, Enum):
    CREATED = "Created"
    READY_FOR_DISPATCH = "Ready for Dispatch"
    DISPATCHED = "Dispatched"
    DELIVERED = "Delivered"


class SalesOrder(Base, TimestampMixin):
    __tablename__ = "sales_orders"

    id: Mapped[int] = mapped_column(primary_key=True)

    so_number: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
    )

    purchase_order_id: Mapped[int] = mapped_column(
        ForeignKey("purchase_orders.id"),
        unique=True,
    )

    total_value: Mapped[float] = mapped_column(
        Numeric(12, 2),
        default=0,
    )

    status: Mapped[SalesOrderStatus] = mapped_column(
        SqlEnum(SalesOrderStatus),
        default=SalesOrderStatus.CREATED,
    )

    purchase_order = relationship(
        "PurchaseOrder",
        back_populates="sales_order",
    )

    items = relationship(
        "SalesOrderItem",
        back_populates="sales_order",
        cascade="all, delete-orphan",
    )