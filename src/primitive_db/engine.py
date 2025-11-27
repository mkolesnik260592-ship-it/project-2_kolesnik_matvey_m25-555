"""Движок для работы с Primitive DB."""
import shlex
import prompt  # noqa
from src.primitive_db.utils import load_metadata, save_metadata
from src.primitive_db.core import create_table, drop_table


def run():
    """Главный игровой цикл"""
    print("***")
    print("Добро пожаловать в Primitive DB!")
    print("Введите 'help' для справки\n")

    METADATA_FILE = "db_meta.json"

    while True:
        metadata = load_metadata(METADATA_FILE)
        user_input = prompt.string("Введите команду: ")
        args = shlex.split(user_input)
        if len(args) == 0:
            continue
        command = args[0]

        match command:
            case 'exit':
                print("Выход из программы...")
                break
            case 'help':
                print_help()
            case 'create_table':
                if len(args) < 3:
                    print('Ошибка: недостаточно аргументов')
                    print('Использование: create_table <имя> <столбец:тип> ...')
                else:
                    table_name = args[1]
                    columns = args[2:]
                    metadata = create_table(metadata, table_name, columns)
                    if table_name in metadata:
                        save_metadata(METADATA_FILE, metadata)
                        print(f'Таблица "{table_name}" создана')
            case 'drop_table':
                if len(args) < 2:
                    print("Ошибка: укажите имя таблицы")
                    print("Использование: drop_table <имя>")
                else:
                    table_name = args[1]
                    if table_name in metadata:
                        metadata = drop_table(metadata, table_name)
                        save_metadata(METADATA_FILE, metadata)
                        print(f'Таблица "{table_name}" удалена')
                    else:
                        print(f'Ошибка: таблица "{table_name}" не существует')
            case 'list_tables':
                if len(metadata) == 0:
                    print("Нет таблиц")
                else:
                    print("Список таблиц:")
                    for table_name, table_data in metadata.items():
                        columns = table_data["columns"]
                        print(f"  {table_name}: {columns}")


def print_help():
    """Выводит на экран сообщение с командами"""

    print("\n***Процесс работы с таблицей***")
    print("Функции:")
    print("<command> create_table <имя_таблицы> <столбец1:тип> .. - создать таблицу")
    print("<command> list_tables - показать список всех таблиц")
    print("<command> drop_table <имя_таблицы> - удалить таблицу")

    print("\nОбщие команды:")
    print("<command> exit - выход из программы")
    print("<command> help - справочная информация\n")
