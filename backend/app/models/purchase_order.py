from enum import Enum

from sqlalchemy import Date, DateTime, Enum as SqlEnum, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from app.models.base import Base, TimestampMixin


class PurchaseOrderStatus(str, Enum):
    UPLOADED = "Uploaded"
    UNDER_REVIEW = "Under Review"
    APPROVED = "Approved"
    PARTIALLY_APPROVED = "Partially Approved"
    REJECTED = "Rejected"


class PurchaseOrder(Base, TimestampMixin):
    __tablename__ = "purchase_orders"

    id: Mapped[int] = mapped_column(primary_key=True)

    po_number: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    delivery_date: Mapped[date] = mapped_column(nullable=False)

    status: Mapped[PurchaseOrderStatus] = mapped_column(
        SqlEnum(PurchaseOrderStatus),
        default=PurchaseOrderStatus.UPLOADED,
        nullable=False,
    )

    total_value: Mapped[float] = mapped_column(
        Numeric(12, 2),
        default=0,
    )

    uploaded_file_id: Mapped[int | None] = mapped_column(
        ForeignKey("uploaded_files.id"),
        nullable=True,
    )

    customer = relationship("User")

    uploaded_file = relationship("UploadedFile")

    items = relationship(
        "PurchaseOrderItem",
        back_populates="purchase_order",
        cascade="all, delete-orphan",
    )

    sales_order = relationship(
        "SalesOrder",
        back_populates="purchase_order",
        uselist=False,
    )