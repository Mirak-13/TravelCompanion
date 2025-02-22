from contextlib import asynccontextmanager

from fastapi import FastAPI
import requests

from database.config import Base
from database.config import db_helper
from api.places.views import router as places_router
from api.hotels.views import router as hotels_router
from api.places.config import url, headers
from api.places.models import recommendations_by_category


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(places_router)
app.include_router(hotels_router)


@app.get("/", tags=["Home"])
async def home():
    recommendation_places = requests.get(url=url, headers=headers, params=recommendations_by_category())
    return "Рекомендации на основе посещенных мест", recommendation_places.json()