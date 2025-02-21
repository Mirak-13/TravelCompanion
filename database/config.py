from pydantic_settings import BaseSettings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class Settings(BaseSettings):
    db_url: str = 'sqlite+aiosqlite:///./db.sqlite3'
    db_echo: bool = True


settings = Settings()


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(url=url, echo=echo)
        self.session = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )


db_helper = DatabaseHelper(url=settings.db_url, echo=settings.db_echo)


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls) -> str:
        return f'{cls.__name__.lower()}s'

    id: Mapped[int] = mapped_column(primary_key=True)
