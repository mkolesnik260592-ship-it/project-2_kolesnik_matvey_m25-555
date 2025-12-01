# Primitive DB

Простая интерактивная база данных на Python с поддержкой CRUD операций и SQL-подобным синтаксисом.

## Описание

Учебный проект CLI-приложения для управления таблицами и данными с демонстрацией:

- Создания Python-пакетов с Poetry
- Интерактивного CLI с библиотекой prompt
- Работы с JSON для хранения данных
- Декораторов Python (обработка ошибок, подтверждение, замер времени)
- Замыканий (кэширование запросов)
- Форматированного вывода с PrettyTable

## Установка

### Требования

- Python 3.10+
- Poetry

### Из исходников

```bash
git clone git@github.com:mkolesnik260592-ship-it/project-2_kolesnik_matvey_m25-555.git
cd project-2_kolesnik_matvey_m25-555
poetry install

Из пакета
pip install dist/project_2_kolesnik_matvey_m25_555-0.1.0-py3-none-any.whl

Использование
# Poetry
make run
# Установленный пакет
database

Команды
Управление таблицами
create_table <имя> <столбец:тип> ...  - Создать таблицу
list_tables                           - Показать все таблицы
drop_table <имя>                      - Удалить таблицу (с подтверждением)

CRUD операции
insert into <таблица> values (...)                     - Добавить запись
select from <таблица> [where ...]                      - Выбрать записи (с кэшированием)
update <таблица> set <столбец = значение> [where ...]  - Обновить записи
delete from <таблица> [where ...]                      - Удалить записи (с подтверждением)

Возможности
Декораторы
@handle_db_errors - Централизованная обработка ошибок

@confirm_action - Запрос подтверждения для критических операций

drop_table users
Вы уверены, что хотите выполнить "удаление таблицы" [y/n]: y

@log_time - Замер времени выполнения

Функция insert выполнилась за 0.002 секунд.

Кэширование
Замыкание create_cacher() кэширует SELECT-запросы:

select from users where name = Sergei
[CACHE] Вычисление результата для ключа: users_{'name': 'Sergei'}
select from users where name = Sergei
[CACHE] Результат найден для ключа: users_{'name': 'Sergei'}

Форматированный вывод
+----+--------+-----+
| ID |  name  | age |
+----+--------+-----+
| 1  | Sergei |  28 |
+----+--------+-----+

Пример работы
$ database
Введите команду: create_table users name:str age:int
Таблица "users" создана
Введите команду: insert into users values ("Sergei", 28)
Запись с ID=1 успешно добавлена в таблицу "users".
Функция insert выполнилась за 0.001 секунд.
Введите команду: select from users
[CACHE] Вычисление результата для ключа: users_all
+----+--------+-----+
| ID |  name  | age |
+----+--------+-----+
| 1  | Sergei |  28 |
+----+--------+-----+
Введите команду: delete from users where name = Sergei
Вы уверены, что хотите выполнить "удаление записи" [y/n]: y
Удалено записей: 1

Структура
src/primitive_db/
├── main.py         - Точка входа
├── engine.py       - Главный цикл и обработка команд
├── core.py         - CRUD операции с декораторами
├── parser.py       - Парсинг SQL-подобных команд
├── decorators.py   - Декораторы и кэширование
└── utils.py        - Работа с JSON

Технологии
Python 3.10+, Poetry, prompt, PrettyTable, shlex, json

Демонстрация

https://asciinema.org/a/qlnzHXLfj5IQpu4DKXfsgqrAr

Автор
Колесник Матвей, М25-555

Лицензия
MIT
