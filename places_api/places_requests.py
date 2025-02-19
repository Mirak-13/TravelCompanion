from fastapi import APIRouter
import requests

from places_api.api_settings import url, headers, places_category, place

router = APIRouter(prefix='/places')


@router.get('/categories', tags=['places'])
async def get_places_category(category: str, city: str, country: str = 'Россия', limit: int = 20):
    response = requests.get(url=url, headers=headers, params=places_category(category, country, limit), )
    return response.json()


@router.get('/', tags=['places'])
async def get_place(name: str, city: str, country: str = ' Россия', limit: int = 20):
    response = requests.get(url=url, headers=headers, params=place(name, city, country, limit), )
    return response.json()