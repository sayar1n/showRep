import uuid
from datetime import datetime

from core.base_model import Base  # noqa
from sqlalchemy import String, UUID, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import mapped_column, Mapped


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    importance: Mapped[bool] = mapped_column(Boolean)
    urgency: Mapped[bool] = mapped_column(Boolean)
    phase: Mapped[str] = mapped_column(String)
    date_of_completion: Mapped[datetime] = mapped_column(DateTime)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)


