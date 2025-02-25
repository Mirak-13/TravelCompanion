from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database.comments.crud import create_comment, get_comment
from database.config import db_helper
from database.comments.schemas import Table, CreateTable

async def get_db():
    async with db_helper.session() as session:
        yield session

router = APIRouter(prefix="/comments", tags=["comments"])

@router.post("/", response_model=Table)
async def add_comment(comment: CreateTable, db: Annotated[AsyncSession, Depends(get_db)]):
    new_comment = await create_comment(db, comment)
    return new_comment

@router.get("/{place_id}", response_model=list[Table])
async def get_comment_by_place(place_id: str, db:AsyncSession = Depends(get_db)):
    comments = await get_comment(db, place_id)
    if not comments:
        raise HTTPException(status_code=404, detail="Отзывы не найдены")
    return comments

