import uuid
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import scoped_session
from sqlalchemy import and_
from fastapi.encoders import jsonable_encoder
from starlette.requests import Request

from auth.security import manager, limiter  # noqa

from core.database import get_session  # noqa
from event.models import Event  # noqa
from event.schemas import EventSchema, CreateEventRequestSchema, CreateEventResponseSchema, UpdateEventRequestSchema, UpdateEventResponseSchema  # noqa


router = APIRouter()


@router.post('/', response_model=CreateEventResponseSchema)
@limiter.limit('100/minute')
async def create_event(
        request: Request,
        data: CreateEventRequestSchema,
        db: scoped_session = Depends(get_session),
        user=Depends(manager)
):
    """
    Create new event
    """
    event = Event(**data.model_dump(), user_id=user.id)
    db.add(event)
    db.commit()
    db.refresh(event)
    return event


@router.patch("/{event_id}", response_model=UpdateEventResponseSchema)
@limiter.limit('100/minute')
async def update_event(
        request: Request,
        event_id: uuid.UUID,
        data: UpdateEventRequestSchema,
        db: scoped_session = Depends(get_session),
        user=Depends(manager)
):
    """
    Update event
    """
    event = db.query(Event).filter(
        and_(
            Event.id == event_id,
            Event.user_id == user.id
        )
    ).first()
    if not event:
        return HTTPException(
            status_code=404,
            detail="Event not found"
        )
    obj_data = jsonable_encoder(event)
    update_data = data.model_dump(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(event, field, update_data[field])
    event.updated_at = datetime.now()
    db.add(event)
    db.commit()
    db.refresh(event)
    return event


@router.get("/", response_model=list[EventSchema])
@limiter.limit("100/minute")
async def get_events(
        request: Request,
        db: scoped_session = Depends(get_session),
        user=Depends(manager)
):
    """
    Get all events.
    """
    return db.query(Event).filter(Event.user_id == user.id).all()


@router.get("/{event_id}", response_model=EventSchema)
@limiter.limit("100/minute")
async def get_event_by_id(
        request: Request,
        event_id: uuid.UUID,
        db: scoped_session = Depends(get_session),
        user=Depends(manager)
):
    """
    Get event by id.
    """
    event = db.query(Event).filter(
        and_(
            Event.id == event_id,
            Event.user_id == user.id
        )
    ).first()
    if not event:
        return HTTPException(
            status_code=404,
            detail="Event not found"
        )
    return event


@router.delete("/{event_id}")
@limiter.limit("100/minute")
async def delete_event(
        request: Request,
        event_id: uuid.UUID,
        db: scoped_session = Depends(get_session),
        user=Depends(manager)
):
    """
    Delete event.
    """
    event = db.query(Event).filter(
        and_(
            Event.id == event_id,
            Event.user_id == user.id
        )
    ).delete()
    if event == 0:
        return HTTPException(
            status_code=404,
            detail="Event not found"
        )
    return {"id": event_id}
