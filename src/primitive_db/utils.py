from pathlib import Path
import json


def load_metadata(filepath):
    """ Загрузка данных """

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data


def save_metadata(filepath, data):
    """ Загрузка данных """

    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def load_table_data(table_name):
    """Загрузка данных таблицы из json файла"""

    data_directory = Path("data")
    data_directory.mkdir(exist_ok=True)
    filepath = data_directory / f"{table_name}.json"
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

def save_table_data(table_name, data):
    """Сохранение данных таблицы из json файла"""
    data_directory = Path("data")
    data_directory.mkdir(exist_ok=True)
    filepath = data_directory / f"{table_name}.json"
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
