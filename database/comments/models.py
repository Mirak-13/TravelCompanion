from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from ..config import CreateTableHelper


class Comment(CreateTableHelper):
    place_id: Mapped[str] = mapped_column(String(24))
    user_name: Mapped[str] = mapped_column(String(30))
    comment: Mapped[str] = mapped_column(String(255))

