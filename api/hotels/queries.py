def query_hotel_name_city(value: str) -> dict:
    params = {
        "query": f"{value}",  # Название отеля
        "lang": "ru",
    }
    return params
