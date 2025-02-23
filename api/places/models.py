import json
from pathlib import Path

from api.places.config import LIMIT, RECOMMENDATION_LIMIT

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def query_by_category(category: str, city: str, country: str = 'Россия', limit: int = LIMIT) -> dict:
    params = {
        "query": f"{category}",
        "near": f"{city}, {country}",
        "limit": limit
    }
    return params


def query_by_name(name: str, city: str, country: str = 'Россия', limit: int = LIMIT) -> dict:
    params = {
        "query": f"{name}",
        "near": f"{city}, {country}",
        "limit": limit
    }
    return params


def recommendations_by_category(city: str = 'Москва', country: str = 'Россия', limit: int = RECOMMENDATION_LIMIT) -> dict:
    try:
        filename = BASE_DIR / "rec_data.json"
        with open(filename, 'r', encoding='utf8') as file:
            data = json.load(file)
            category = int(next(iter(data.keys())))

    except FileNotFoundError:
        print('Файл не найден!')
    except json.JSONDecodeError:
        print('Некорректный JSON!')

    params = {
        "categories": category,
        "near": f"{city}, {country}",
        "limit": limit,
    }
    return params
