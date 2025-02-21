import json
from typing import Any


def save_data(data: Any) -> str:
    try:
        filename = 'rec_data.json'

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                existing_data = json.load(file)
                if not isinstance(existing_data, list):
                    existing_data = [existing_data]
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []

        existing_data.append(data)

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(existing_data, file, ensure_ascii=False, indent=4)

        return 'Данные успешно добавлены.'

    except Exception as e:
        return f'Ошибка: {e}'
