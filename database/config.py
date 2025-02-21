from pydantic_settings import BaseSettings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


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
