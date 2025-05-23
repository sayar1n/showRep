from datetime import datetime
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import scoped_session
from sqlalchemy import and_
from fastapi.encoders import jsonable_encoder
from starlette.requests import Request

from auth.security import manager, limiter  # noqa

from core.database import get_session  # noqa
from note.models import Note  # noqa
from note.schemas import NoteSchema, CreateNoteRequestSchema, CreateNoteResponseSchema, UpdateNoteRequestSchema, UpdateNoteResponseSchema  # noqa

router = APIRouter()


@router.post('/', response_model=CreateNoteResponseSchema)
@limiter.limit("100/minute")
async def create_note(
        request: Request,
        data: CreateNoteRequestSchema,
        db: scoped_session = Depends(get_session),
        user=Depends(manager)
):
    """
    Create new note.
    """
    note = Note(**data.model_dump(), user_id=user.id)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


@router.patch("/{note_id}", response_model=UpdateNoteResponseSchema)
@limiter.limit("100/minute")
async def update_note(
        request: Request,
        note_id: UUID,
        data: UpdateNoteRequestSchema,
        db: scoped_session = Depends(get_session),
        user=Depends(manager)
):
    """
    Update note.
    """
    note = db.query(Note).filter(
        and_(
            Note.id == note_id,
            Note.user_id == user.id
        )
    ).first()
    if not note:
        return HTTPException(
            status_code=404,
            detail="Note not found"
        )
    obj_data = jsonable_encoder(note)  # noqa
    update_data = data.model_dump(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(note, field, update_data[field])
    note.updated_at = datetime.now()
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


@router.get("/", response_model=list[NoteSchema])
@limiter.limit("100/minute")
async def get_notes(
        request: Request,
        db: scoped_session = Depends(get_session),
        user=Depends(manager)
):
    """
    Get all notes.
    """
    return db.query(Note).filter(Note.user_id == user.id).all()


@router.get("/{note_id}", response_model=NoteSchema)
@limiter.limit("100/minute")
async def get_note_by_id(
        request: Request,
        note_id: UUID,
        db: scoped_session = Depends(get_session),
        user=Depends(manager)
):
    """
    Get note by id.
    """
    note = db.query(Note).filter(
        and_(
            Note.id == note_id,
            Note.user_id == user.id
        )
    ).first()
    if not note:
        return HTTPException(
            status_code=404,
            detail="Note not found"
        )
    return note


@router.delete("/{note_id}")
@limiter.limit("100/minute")
async def delete_note(
        request: Request,
        note_id: UUID,
        db: scoped_session = Depends(get_session),
        user=Depends(manager)
):
    """
    Delete note.
    """
    note = db.query(Note).filter(
        and_(
            Note.id == note_id,
            Note.user_id == user.id
        )
    ).delete()
    if note == 0:
        return HTTPException(
            status_code=404,
            detail="Note not found"
        )
    return {"id": note_id}
