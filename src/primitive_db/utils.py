"""Утилиты для работы с файлами."""
import json
from pathlib import Path

from .constants import DATA_DIR


def load_metadata(filepath):
    """Загрузка метаданных из JSON файла."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data


def save_metadata(filepath, data):
    """Сохранение метаданных в JSON файл."""
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def load_table_data(table_name):
    """Загрузка данных таблицы из JSON файла."""
    data_directory = Path(DATA_DIR)
    data_directory.mkdir(exist_ok=True)
    filepath = data_directory / f"{table_name}.json"
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data


def save_table_data(table_name, data):
    """Сохранение данных таблицы в JSON файл."""
    data_directory = Path(DATA_DIR)
    data_directory.mkdir(exist_ok=True)
    filepath = data_directory / f"{table_name}.json"
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
