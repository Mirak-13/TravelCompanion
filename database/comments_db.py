from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from .config import Base


class Comments(Base):
    name: Mapped[str] = mapped_column(String(30))
    comment: Mapped[str] = mapped_column(String(255))
