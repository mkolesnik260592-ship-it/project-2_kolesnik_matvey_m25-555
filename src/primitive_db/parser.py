"""Парсинг команд для работы с данными."""

def parse_where_clause(where_string):

    if not where_string:
        return None

    parts = where_string.split('=')
    if len(parts) != 2:
        return None
    column = parts[0].strip()
    value = parts[1].strip()

    if value.startswith('"') and value.endswith('"'):
        value = value[1:-1]
    elif value.startswith("'") and value.endswith("'"):
        value = value[1:-1]

    return {column: value}

def parse_values(values_string):

    values_string = values_string.strip()
    if values_string.startswith('(') and values_string.endswith(')'):
        values_string = values_string[1:-1]

    values = []
    current = ""
    in_quotes = False
    quote_char = None

    for char in values_string:
        if char in ("'", '"') and not in_quotes:
            in_quotes = True
            quote_char = char
        elif char == quote_char and in_quotes:
            in_quotes = False
            quote_char = None
        elif char == ',' and not in_quotes:
            values.append(current.strip())
            current = ""
        else:
            current += char

    if current.strip():
        values.append(current.strip())

    cleaned_values = []
    for val in values:
        val = val.strip()
        if val.startswith('"') and val.endswith('"'):
            val = val[1:-1]
        elif val.startswith("'") and val.endswith("'"):
            val = val[1:-1]
        cleaned_values.append(val)

    return cleaned_values

def parse_set_clause(set_string):
    return parse_where_clause(set_string)
