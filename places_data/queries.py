import json
from typing import Any


def save_data(data: Any) -> str:
    """Добавляет id категории мест из запросов и сортирует по количеству запросов к данной категории."""
    try:
        filename = 'rec_data.json'

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                existing_data = json.load(file)
                if not isinstance(existing_data, dict):
                    existing_data = {}
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = {}

        for i in data['results']:
            cat = str(i['categories'][0]['id'])
            existing_data[cat] = existing_data.get(cat, 0) + 1

        existing_data = dict(sorted(existing_data.items(), key=lambda item: item[1], reverse=True))

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(existing_data, file, ensure_ascii=False, indent=4)

        return 'Данные успешно добавлены.'

    except Exception as e:
        return f'Ошибка: {e}'
