from collections import defaultdict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from api.places.config import LIMIT
from models import Comment
from schemas import Table


async def create_comments(db: AsyncSession, table: Table):
    comment_table = Table(place_id=table.place_id, name=table.name, comment=table.comment)
    db.add(comment_table)
    await db.commit()
    await db.refresh(comment_table)
    return comment_table


async def get_comments(db: AsyncSession, skip: int = 0, limit: int = LIMIT):
    query = select(Comment).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()

async def update_comments(db: AsyncSession, item_id: int, item_update: Table):
    query = select(Comment).where(Comment.place_id == item_id)
    result = await db.execute(query)
    item = await result.scalars().first()

    if not item:
        return None

    item.place_id = item_update.place_id
    item.name = item_update.name
    item.comment = item_update.comment

    await db.commit()
    await db.refresh(item)
    return item

