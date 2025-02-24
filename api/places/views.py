import sys
import os

import requests
from fastapi import APIRouter

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from places_data.models import save_data
from api.places.config import url, headers, LIMIT
from api.places.queries import query_by_category, query_by_name

router = APIRouter(prefix='/places')


@router.get('/', tags=['places'])
async def get_by_name(name: str, city: str, country: str = 'Россия', limit: int = LIMIT) -> dict:
    """Отображает места по названиям."""
    response = requests.get(url=url, headers=headers, params=query_by_name(name, city, country, limit), )
    save_data(response.json())
    return response.json()


@router.get('/categories', tags=['places'])
async def get_by_category(category: str, city: str, country: str = 'Россия', limit: int = LIMIT) -> dict:
    """Отображает места по категориям."""
    response = requests.get(url=url, headers=headers, params=query_by_category(category, city, country, limit), )
    save_data(response.json())

    return response.json()
