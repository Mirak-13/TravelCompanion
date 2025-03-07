import json
from pathlib import Path

from api.places.config import LIMIT, RECOMMENDATION_LIMIT

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def query(parameter: str, city: str, country: str = 'Россия', limit: int = LIMIT) -> dict:
    params = {
        "query": f"{parameter}",
        "near": f"{city}, {country}",
        "limit": limit
    }
    return params


def recommendations_by_category(city: str = 'Москва', country: str = 'Россия',
                                limit: int = RECOMMENDATION_LIMIT) -> dict | None:
    try:
        filename = BASE_DIR / "recommendations_data.json"
        with open(filename, 'r', encoding='utf8') as file:
            data = json.load(file)

            if not data:
                print('Файл пуст или не содержит данных!')
                return None

            category = list(data.keys())[0]

            if not category:
                print('Нет доступных категорий!')
                return None

    except FileNotFoundError:
        print('Файл не найден!')
        return None
    except json.JSONDecodeError:
        print('Некорректный JSON!')
        return None

    params = {
        "categories": category,
        "near": f"{city}, {country}",
        "limit": limit,
    }
    return params
