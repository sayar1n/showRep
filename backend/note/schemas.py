from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class NoteSchema(BaseModel):
    """
    Note schema.
    """
    id: UUID
    title: str
    description: str
    created_at: datetime
    updated_at: datetime | None = None


class CreateNoteRequestSchema(BaseModel):
    """
    Creates note request schema.
    """
    title: str
    description: str


class CreateNoteResponseSchema(BaseModel):
    """
    Create note response schema.
    """
    id: UUID
    title: str
    description: str
    created_at: datetime


class UpdateNoteRequestSchema(BaseModel):
    """
    Update note request schema.
    """
    title: str | None = None
    description: str | None = None


class UpdateNoteResponseSchema(BaseModel):
    """
    Update note response schema.
    """
    id: UUID
    title: str
    description: str
    updated_at: datetime

