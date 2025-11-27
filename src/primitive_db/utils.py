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
