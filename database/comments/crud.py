
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from api.places.config import LIMIT
from database.comments.models import Comment
from database.comments.schemas import Table, CreateTable


async def create_comment(db: AsyncSession, table: CreateTable):
    comment_table = Comment(place_id=table.place_id, user_name=table.user_name, comment=table.comment)
    db.add(comment_table)
    await db.commit()
    await db.refresh(comment_table)
    return comment_table


async def get_comment(db: AsyncSession, place_id: str, skip: int = 0, limit: int = LIMIT):
    query = select(Comment).where(Comment.place_id == place_id).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()
