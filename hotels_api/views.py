from fastapi import APIRouter
import requests

from general.models import save_data
from hotels_api.config import url
from hotels_api.models import query_hotels

router = APIRouter(prefix='/hotels')

@router.get('/', tags=['hotels'])
async def get_hotels(query: str) -> dict:
    """Отображает отели по названиям и городам.
    Запрос пишется в одну строчку сначала название потом необязательный параметр город."""
    response = requests.get(url=url, params=query_hotels(query), )
    save_data(response.json())
    return response.json()
