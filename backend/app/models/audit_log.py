from sqlalchemy import ForeignKey, JSON, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin


class AuditLog(Base, TimestampMixin):
    __tablename__ = "audit_logs"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    entity: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    entity_id: Mapped[int] = mapped_column(nullable=False)

    action: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    old_value: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    new_value: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    user = relationship("User")