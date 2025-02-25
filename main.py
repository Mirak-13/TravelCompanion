from contextlib import asynccontextmanager

from fastapi import FastAPI
import requests

from database.config import CreateTableHelper
from database.config import db_helper
from api.places.views import router as places_router
from api.hotels.views import router as hotels_router
from database.comments.views import router as comments_router
from api.places.config import url, headers, RECOMMENDATION_LIMIT
from api.places.queries import recommendations_by_category


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(CreateTableHelper.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(places_router)
app.include_router(hotels_router)
app.include_router(comments_router)


@app.get("/", tags=["Home"])
async def home(category: int = recommendations_by_category()['categories'], city: str = "Москва",
               country: str = 'Россия',
               limit=RECOMMENDATION_LIMIT):
    if recommendations_by_category() is not None:
        recommendation_places = requests.get(url=url, headers=headers,
                                             params=recommendations_by_category(city=city, country=country,
                                                                                limit=limit))
        return "Рекомендации на основе посещенных мест:", recommendation_places.json()
    else:
        return None
