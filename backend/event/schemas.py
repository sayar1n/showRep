from datetime import datetime
import uuid
from pydantic import BaseModel


class EventSchema(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    date_of_event: datetime
    created_at: datetime
    updated_at: datetime | None = None


class CreateEventRequestSchema(BaseModel):
    title: str
    description: str
    date_of_event: datetime


class CreateEventResponseSchema(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    date_of_event: datetime
    created_at: datetime


class UpdateEventRequestSchema(BaseModel):
    title: str | None = None
    description: str | None = None
    date_of_event: datetime | None = None


class UpdateEventResponseSchema(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    date_of_event: datetime
    updated_at: datetime
