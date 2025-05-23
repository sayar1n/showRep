import uuid
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import scoped_session
from sqlalchemy import and_
from fastapi.encoders import jsonable_encoder
from starlette.requests import Request

from auth.security import manager, limiter  # noqa

from core.database import get_session  # noqa
from task.models import Task  # noqa
from task.schemas import TaskSchema, CreateTaskRequestSchema, CreateTaskResponseSchema, UpdateTaskRequestSchema, UpdateTaskResponseSchema  # noqa


router = APIRouter()


@router.post('/', response_model=CreateTaskResponseSchema)
@limiter.limit('100/second')
async def create_task(
        request: Request,
        data: CreateTaskRequestSchema,
        db: scoped_session = Depends(get_session),
        user=Depends(manager)
):
    """
    Create new task
    """
    task = Task(**data.model_dump(), user_id=user.id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@router.patch("/{task_id}", response_model=UpdateTaskResponseSchema)
@limiter.limit("100/minute")
async def update_task(
        request: Request,
        task_id: uuid.UUID,
        data: UpdateTaskRequestSchema,
        db: scoped_session = Depends(get_session),
        user=Depends(manager)
):

    """
    Update task.
    """
    task = db.query(Task).filter(
        and_(
            Task.id == task_id,
            Task.user_id == user.id
        )
    ).first()
    if not task:
        return HTTPException(
            status_code=404,
            detail="Task not found"
        )
    obj_data = jsonable_encoder(task)  # noqa
    update_data = data.model_dump(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(task, field, update_data[field])
    task.updated_at = datetime.now()
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@router.get("/", response_model=list[TaskSchema])
@limiter.limit("100/minute")
async def get_tasks(
        request: Request,
        db: scoped_session = Depends(get_session),
        user=Depends(manager)
):
    """
    Get all tasks.
    """
    return db.query(Task).filter(Task.user_id == user.id).all()


@router.get("/{task_id}", response_model=TaskSchema)
@limiter.limit("100/minute")
async def get_task_by_id(
        request: Request,
        task_id: uuid.UUID,
        db: scoped_session = Depends(get_session),
        user=Depends(manager)
):
    """
    Get task by id.
    """
    task = db.query(Task).filter(
        and_(
            Task.id == task_id,
            Task.user_id == user.id
        )
    ).first()
    if not task:
        return HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return task


@router.delete("/{task_id}")
@limiter.limit("100/minute")
async def delete_task(
        request: Request,
        task_id: uuid.UUID,
        db: scoped_session = Depends(get_session),
        user=Depends(manager)
):
    """
    Delete task.
    """
    task = db.query(Task).filter(
        and_(
            Task.id == task_id,
            Task.user_id == user.id
        )
    ).delete()
    if task == 0:
        return HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return {"id": task_id}

