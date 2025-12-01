import os

from .constants import DATA_DIR, VALID_TYPES
from .decorators import confirm_action, handle_db_errors, log_time


@handle_db_errors
def create_table(metadata, table_name, columns):
    """ Создание таблицы """

    if table_name in metadata:
        print(f'Ошибка: {table_name} уже есть в {metadata}')
        return metadata

    columns.insert(0, "ID:int")

    for column in columns:
        parts = column.split(":")
        column_type = parts[1]

        if column_type not in VALID_TYPES:
            print(f'Ошибка: недопустимый тип "{column_type}"')
            return metadata

    metadata[table_name] = {"columns": columns}
    return metadata

@handle_db_errors
@confirm_action("удаление таблицы")
def drop_table(metadata, table_name):
    """ Удаление таблицы """

    if table_name not in metadata:
        print(f'Ошибка: {table_name} нет в {metadata}')
        return metadata

    metadata.pop(table_name)
    data_file = f'{DATA_DIR}/{table_name}.json'
    if os.path.exists(data_file):
        os.remove(data_file)
    return metadata


def validate_value(value, expected_type):
    """Валидация значения по типу"""

    if expected_type == 'int':
        try:
            return int(value)
        except ValueError:
            return None
    elif expected_type == 'str':
        return str(value)
    elif expected_type == 'bool':
        if value.lower() in ('true', '1', 'yes'):
            return True
        elif value.lower() in ('false', '0', 'no'):
            return False
        else:
            return None
    return None

@handle_db_errors
@log_time
def insert(metadata, table_name, values, table_data):
    """Добавление записи в таблицу"""

    if table_name not in metadata:
        print(f'Ошибка: Таблица {table_name} не существует')
        return table_data
    columns = metadata[table_name]['columns']

    if len(values) != len(columns) - 1:
        expected = len(columns) - 1
        print(f'Ошибка: ожидается {expected} значений, а получено {len(values)}.')
        return table_data

    if table_data:
        new_id = max(record['ID'] for record in table_data) + 1
    else:
        new_id = 1

    new_record = {'ID': new_id}
    for i, value in enumerate(values):
        column_def = columns[i + 1]
        column_name, column_type = column_def.split(':')
        validated_value = validate_value(value, column_type)
        if validated_value is None:
            print('Ошибка: неверный тип...')
            return table_data
        new_record[column_name] = validated_value


    table_data.append(new_record)
    print(f'Запись с ID={new_id} успешно добавлена в таблицу "{table_name}".')

    return table_data

@handle_db_errors
@log_time
def select(table_data, where_clause):
    """Выборка записей из таблицы"""

    if where_clause is None:
        return table_data

    column_name = list(where_clause.keys())[0]
    value = where_clause[column_name]

    result = []
    for record in table_data:
        record_value = record.get(column_name)
        if str(record_value).lower() == value.lower():
            result.append(record)
    return result

@handle_db_errors
def update(table_data, set_clause, where_clause):
    """Обновление записей в таблице"""

    set_column = list(set_clause.keys())[0]
    set_value = set_clause[set_column]

    updated_count = 0

    for record in table_data:
        matches = False

        if where_clause is None:
            matches = True
        else:
            where_column = list(where_clause.keys())[0]
            where_value = where_clause[where_column]

            if where_column in record and str(record[where_column]) == where_value:
                matches = True

        if matches:
            if set_column in record:
                current_value = record[set_column]

                if isinstance(current_value, int):
                    record[set_column] = int(set_value)
                elif isinstance(current_value, bool):
                    record[set_column] = set_value.lower() in ('true', '1', 'yes')
                else:
                    record[set_column] = set_value

                updated_count += 1

    print(f'Обновлено записей: {updated_count}')

    return table_data

@handle_db_errors
@confirm_action("удаление записи")
def delete(table_data, where_clause):
    """Удаление записей из таблицы"""

    if where_clause is None:
        count = len(table_data)
        table_data.clear()
        print(f'Удалено записей: {count}')
        return table_data

    where_column = list(where_clause.keys())[0]
    where_value = where_clause[where_column]

    new_table_data = []
    deleted_count = 0

    for record in table_data:
        if where_column in record and str(record[where_column]) == where_value:
            deleted_count += 1
        else:
            new_table_data.append(record)

    print(f'Удалено записей: {deleted_count}')

    return new_table_data
