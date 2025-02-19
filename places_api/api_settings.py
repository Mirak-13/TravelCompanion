import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv('API_KEY')

url = "https://api.foursquare.com/v3/places/search"

headers = {
    "accept": "application/json",
    "Accept-Language": "ru",
    "Authorization": API_KEY,
}


def places_category(category: str, city: str, country: str = 'Россия', limit: int = 20) -> dict:
    params = {
        "query": f"{category}",
        "near": f"{city}, {country}",
        "limit": limit
    }
    return params


def place(name: str, city: str, country: str = 'Россия', limit: int = 20):
    params = {
        "query": f"{name}",
        "near": f"{city}, {country}",
        "limit": limit
    }
    return params
