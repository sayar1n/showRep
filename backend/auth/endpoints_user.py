from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy import and_
from sqlalchemy.orm import scoped_session

from starlette.requests import Request

from auth.models import User  # noqa
from auth.schemas import SettingsRequestSchema, SettingsResponseSchema, DeleteUserRequestSchema, DeleteUserResponseSchema  # noqa
from auth.security import manager, limiter  # noqa
from core.database import get_session  # noqa

from auth.security import pwd_context

router = APIRouter()


@router.patch("/settings", response_model=SettingsResponseSchema)
async def update_settings(
        request: Request,
        data: SettingsRequestSchema,
        db: scoped_session = Depends(get_session),
        user=Depends(manager)
):
    us = db.query(User).get(user.id)
    obj_data = jsonable_encoder(us)
    update_data = data.model_dump(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(us, field, update_data[field])
    us.password = pwd_context.hash(us.password)
    db.add(us)
    db.commit()
    db.refresh(us)
    return us


@router.delete("/settings", response_model=DeleteUserResponseSchema)
async def delete_account(
        request: Request,
        data: DeleteUserRequestSchema,
        db: scoped_session = Depends(get_session),
        user=Depends(manager)
):
    us = db.query(User).get(user.id)
    if not us:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    if not pwd_context.verify(data.password, us.password):
        raise HTTPException(status_code=400, detail="Неверный пароль")

    db.delete(us)
    db.commit()
    return {"detail": "Аккаунт успешно удален"}
