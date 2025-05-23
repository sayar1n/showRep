from datetime import datetime
import uuid
from pydantic import BaseModel


class TaskSchema(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    importance: bool
    urgency: bool
    phase: str
    date_of_completion: datetime
    created_at: datetime
    updated_at: datetime | None = None


class CreateTaskRequestSchema(BaseModel):
    title: str
    description: str
    importance: bool
    urgency: bool
    phase: str
    date_of_completion: datetime


class CreateTaskResponseSchema(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    importance: bool
    urgency: bool
    phase: str
    date_of_completion: datetime
    created_at: datetime


class UpdateTaskRequestSchema(BaseModel):
    title: str | None = None
    description: str | None = None
    importance: bool | None = None
    urgency: bool | None = None
    phase: str | None = None
    date_of_completion: datetime | None = None


class UpdateTaskResponseSchema(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    importance: bool
    urgency: bool
    phase: str
    date_of_completion: datetime
    updated_at: datetime

