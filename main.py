from contextlib import asynccontextmanager

from database.config import Base
from database.config import db_helper
from fastapi import FastAPI
from api.places.views import router as places_router
from api.hotels.views import router as hotels_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(places_router)
app.include_router(hotels_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
