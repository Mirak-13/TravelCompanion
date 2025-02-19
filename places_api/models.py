def query_by_category(category: str, city: str, country: str = 'Россия', limit: int = 20) -> dict:
    """Запрашивает места по категориям."""
    params = {
        "query": f"{category}",
        "near": f"{city}, {country}",
        "limit": limit
    }
    return params


def query_by_name(name: str, city: str, country: str = 'Россия', limit: int = 20) -> dict:
    """Запрашивает места по названиям."""
    params = {
        "query": f"{name}",
        "near": f"{city}, {country}",
        "limit": limit
    }
    return params

