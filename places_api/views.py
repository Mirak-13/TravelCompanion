from fastapi import APIRouter
import requests

from places_api.config import url, headers
from models import query_by_category, query_by_name

router = APIRouter(prefix='/places')


@router.get('/categories', tags=['places'])
async def get_by_category(category: str, city: str, country: str = 'Россия', limit: int = 20) -> dict:
    """Отображает места по категориям."""
    response = requests.get(url=url, headers=headers, params=query_by_category(category, city, country, limit), )
    return response.json()


@router.get('/', tags=['places'])
async def get_by_name(name: str, city: str, country: str = 'Россия', limit: int = 20) -> dict:
    """Отображает места по названиям."""
    response = requests.get(url=url, headers=headers, params=query_by_name(name, city, country, limit), )
    return response.json()