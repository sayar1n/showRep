import uuid
from datetime import datetime

from sqlalchemy import String, UUID, DateTime, ARRAY
from sqlalchemy.orm import mapped_column, Mapped

from core.base_model import Base


class User(Base):

    __tablename__ = "users"  # noqa

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    photo: Mapped[str | None] = mapped_column(String, nullable=True)
    location: Mapped[str | None] = mapped_column(String, nullable=True)
    work_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    status: Mapped[str | None] = mapped_column(String, nullable=True)
    languages: Mapped[list[str] | None] = mapped_column(ARRAY(String), nullable=True)
    social: Mapped[list[str] | None] = mapped_column(ARRAY(String), nullable=True)
    last_login_date: Mapped[list[datetime]] = mapped_column(ARRAY(DateTime),
                                                            default=lambda: [datetime.now()], nullable=False)
    tasks: Mapped[list[str]] = mapped_column(type_=ARRAY(String), nullable=True)
    notes: Mapped[list[str]] = mapped_column(type_=ARRAY(String), nullable=True)
    events: Mapped[list[str]] = mapped_column(type_=ARRAY(String), nullable=True)
