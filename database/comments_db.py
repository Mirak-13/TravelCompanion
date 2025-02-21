from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from .config import Base


class Comment(Base):
    user_name: Mapped[str] = mapped_column(String(30))
    comment: Mapped[str] = mapped_column(String(255))
