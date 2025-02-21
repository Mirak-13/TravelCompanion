from fastapi import APIRouter
import requests

from places_data.models import save_data
from api.hotels.config import url
from api.hotels.models import query_hotel_name_city

router = APIRouter(prefix='/hotels')

@router.get('/', tags=['hotels'])
async def get_hotels(query: str) -> dict:
    """Отображает отели по названиям и городам.
    Запрос пишется в одну строчку сначала название потом необязательный параметр город."""
    response = requests.get(url=url, params=query_hotel_name_city(query), )
    save_data(response.json())
    return response.json()
