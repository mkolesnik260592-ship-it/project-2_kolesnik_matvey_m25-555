def create_table(metadata, table_name, columns):
    """ Создание таблицы """
    if table_name in metadata:
        print(f'Ошибка: {table_name} уже есть в {metadata}')
        return metadata

    columns.insert(0, "ID:int")

    for column in columns:
        parts = column.split(":")
        column_type = parts[1]

        if column_type not in ['int', 'str', 'bool']:
            print(f'Ошибка: недопустимый тип "{column_type}"')
            return metadata

    metadata[table_name] = {"columns": columns}
    return metadata

def drop_table(metadata, table_name):
    """ Удаление таблицы """
    if table_name not in metadata:
        print(f'Ошибка: {table_name} нет в {metadata}')
        return metadata

    metadata.pop(table_name)
    return metadata
