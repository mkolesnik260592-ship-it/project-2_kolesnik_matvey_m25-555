"""Движок для работы с Primitive DB."""
import shlex

import prompt  # type: ignore
from prettytable import PrettyTable  # type: ignore

from .constants import METADATA_FILE, MSG_EXIT, MSG_WELCOME
from .core import create_table, drop_table
from .decorators import create_cacher
from .utils import load_metadata, save_metadata

query_cache = create_cacher()

def run():
    """Главный игровой цикл"""
    print(MSG_WELCOME)

    while True:
        metadata = load_metadata(METADATA_FILE)
        user_input = prompt.string("Введите команду: ")
        args = shlex.split(user_input)
        if len(args) == 0:
            continue
        command = args[0]

        match command:
            case 'exit':
                print(MSG_EXIT)
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
                        if table_name not in metadata:
                            save_metadata(METADATA_FILE, metadata)
                            print(f'Таблица "{table_name}" удалена')
                    else:
                        print(f'Ошибка: таблица "{table_name}" не существует')
            case 'list_tables':
                if len(metadata) == 0:
                    print("Нет таблиц")
                else:
                    table = PrettyTable()
                    table.field_names = ["Таблица", "Столбцы"]

                    for table_name, table_data in metadata.items():
                        columns = ', '.join(table_data["columns"])
                        table.add_row([table_name, columns])

                    print("\nСписок таблиц:")
                    print(table)
            case 'insert':
                if len(args) < 5 or args[1] != 'into' or args[3] != 'values':
                    print('Ошибка: неверный формат команды insert')
                    print('Формат: insert into <table> values (...)')
                    continue

                table_name = args[2]
                values_string = ' '.join(args[4:])

                from .parser import parse_values
                values = parse_values(values_string)

                from .utils import load_table_data, save_table_data
                table_data = load_table_data(table_name)

                from .core import insert
                table_data = insert(metadata, table_name, values, table_data)

                save_table_data(table_name, table_data)
            case 'select':
                if len(args) < 3 or args[1] != 'from':
                    print('Ошибка: неверный формат команды select')
                    print('Формат: select from <table> [where ...]')
                    continue

                table_name = args[2]
                where_clause = None
                if len(args) > 3 and args[3] == 'where':
                    where_string = ' '.join(args[4:])
                    from .parser import parse_where_clause
                    where_clause = parse_where_clause(where_string)

                if where_clause:
                    cache_key = f'{table_name}_{where_clause}'
                else:
                    cache_key = f'{table_name}_all'

                def get_data():
                    from .utils import load_table_data
                    table_data = load_table_data(table_name)

                    from .core import select
                    return select(table_data, where_clause)
                result = query_cache(cache_key, get_data)

                if result:
                    table = PrettyTable()
                    table.field_names = list(result[0].keys())
                    for record in result:
                        table.add_row(list(record.values()))
                    print(table)
                else:
                    print('Записей не найдено.')
            case 'update':
                if len(args) < 5 or args[2] != 'set':
                    print('Ошибка: неверный формат команды update')
                    print('Формат: update <table> set <column = value> [where ...]')
                    continue

                table_name = args[1]


                where_index = -1
                for i, part in enumerate(args):
                    if part == 'where':
                        where_index = i
                        break


                if where_index > 0:
                    set_string = ' '.join(args[3:where_index])
                    where_string = ' '.join(args[where_index + 1:])
                else:
                    set_string = ' '.join(args[3:])
                    where_string = None

                from .parser import parse_set_clause, parse_where_clause
                set_clause = parse_set_clause(set_string)
                where_clause = (
                    parse_where_clause(where_string) if where_string else None
                )

                from .utils import load_table_data, save_table_data
                table_data = load_table_data(table_name)

                from .core import update
                table_data = update(table_data, set_clause, where_clause)

                save_table_data(table_name, table_data)
            case 'delete':

                if len(args) < 3 or args[1] != 'from':
                    print('Ошибка: неверный формат команды delete')
                    print('Формат: delete from <table> [where ...]')
                    continue

                table_name = args[2]

                where_clause = None
                if len(args) > 3 and args[3] == 'where':
                    where_string = ' '.join(args[4:])
                    from .parser import parse_where_clause
                    where_clause = parse_where_clause(where_string)

                from .utils import load_table_data, save_table_data
                table_data = load_table_data(table_name)

                from .core import delete
                table_data = delete(table_data, where_clause)

                save_table_data(table_name, table_data)


def print_help():
    """Выводит на экран сообщение с командами"""

    print("\n*** Primitive DB - Справка ***")
    print("\n=== Управление таблицами ===")
    print("create_table <имя> <столбец:тип> ... - создать таблицу")
    print("list_tables                          - показать список всех таблиц")
    print("drop_table <имя>                     - удалить таблицу")

    print("\n=== CRUD операции ===")
    print("insert into <таблица> values (...)                     - добавить запись")
    print("select from <таблица> [where <столбец> = <значение>]   - выбрать записи")
    print("update <таблица> set <столбец> = <значение> [where ...] - обновить записи")
    print("delete from <таблица> [where <столбец> = <значение>]   - удалить записи")

    print("\n=== Общие команды ===")
    print("help - справочная информация")
    print("exit - выход из программы\n")
