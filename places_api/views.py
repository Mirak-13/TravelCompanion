import sys
import os
from fastapi import APIRouter
import requests

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from general.models import save_data

from places_api.config import url, headers
from places_api.models import query_by_category, query_by_name


router = APIRouter(prefix='/places')


@router.get('/', tags=['places'])
async def get_by_name(name: str, city: str, country: str = 'Россия', limit: int = 20) -> dict:
    """Отображает места по названиям."""
    response = requests.get(url=url, headers=headers, params=query_by_name(name, city, country, limit), )
    save_data(response.json())
    return response.json()


@router.get('/categories', tags=['places'])
async def get_by_category(category: str, city: str, country: str = 'Россия', limit: int = 20) -> dict:
    """Отображает места по категориям."""
    response = requests.get(url=url, headers=headers, params=query_by_category(category, city, country, limit), )
    save_data(response.json())

    return response.json()
