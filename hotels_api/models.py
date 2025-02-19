def query_hotels(value: str) -> dict:
    """Запрашивает отели по названиям и городам."""
    params = {
        "query": f"{value}",  # Название отеля
        "lang": "ru",
    }
    return params
