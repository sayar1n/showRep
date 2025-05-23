from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class RegisterUserRequestSchema(BaseModel):
    username: str
    email: str
    password: str


class SettingsRequestSchema(BaseModel):
    username: str | None = None
    email: str | None = None
    password: str | None = None
    photo: str | None = None
    location: str | None = None
    work_time: datetime | None = None
    status: str | None = None
    languages: list[str] | None = None
    social: list[str] | None = None


class SettingsResponseSchema(BaseModel):
    username: str
    email: str
    password: str
    photo: str
    location: str
    work_time: datetime
    status: str
    languages: list[str]
    social: list[str]

class DeleteUserRequestSchema(BaseModel):
    password: str


class DeleteUserResponseSchema(BaseModel):
    detail: str
