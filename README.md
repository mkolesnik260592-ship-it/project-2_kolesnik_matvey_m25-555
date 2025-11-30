# Primitive DB

Простая интерактивная база данных на Python с поддержкой CRUD операций и SQL-подобным синтаксисом команд.

## Описание

Primitive DB — это учебный проект CLI-приложения для управления таблицами и данными, демонстрирующий:

- Создание Python-пакетов с Poetry
- Интерактивный CLI с библиотекой `prompt`
- Работу с JSON для хранения метаданных и данных
- Организацию кода в модули (OOP, парсинг команд, CRUD операции)
- Типизацию и валидацию данных
- SQL-подобный синтаксис команд

## Установка

### Требования

- Python 3.10+
- Poetry

### Установка из исходников

```bash
# Клонировать репозиторий
git clone git@github.com:mkolesnik260592-ship-it/project-2_kolesnik_matvey_m25-555.git
cd project-2_kolesnik_matvey_m25-555
# Установить зависимости
poetry install

Установка из пакета
# После сборки пакета
pip install dist/primitive_db-0.1.0-py3-none-any.whl

Использование
Запуск через Poetry
poetry run python -m src.primitive_db.main

Запуск через Makefile
make run

Запуск установленного пакета
primitive-db

Команды
Управление таблицами
Команда	Описание
create_table <имя> <столбец:тип> ...	Создать новую таблицу
list_tables	Показать все таблицы
drop_table <имя>	Удалить таблицу
CRUD операции
Команда	Описание
insert into <таблица> values (...)	Добавить запись
select from <таблица> [where ...]	Выбрать записи
update <таблица> set <столбец = значение> [where ...]	Обновить записи
delete from <таблица> [where ...]	Удалить записи
Общие команды
Команда	Описание
help	Показать справку
exit	Выйти из программы
Подробное описание команд
1. create_table — Создание таблицы
Синтаксис:

create_table <имя_таблицы> <столбец1:тип> <столбец2:тип> ...

Описание:
Создаёт новую таблицу с указанными столбцами. Автоматически добавляется столбец ID:int в начало.

Поддерживаемые типы данных:

int — целые числа
str — строки
bool — логические значения
Примеры:

create_table users name:str age:int active:bool
create_table products title:str price:int available:bool
create_table orders user_id:int product_id:int quantity:int

Успешный результат:

Таблица "users" создана

2. list_tables — Список таблиц
Синтаксис:

list_tables

Описание:
Показывает список всех созданных таблиц с их структурой.

Пример результата:

Список таблиц:
  users: ['ID:int', 'name:str', 'age:int', 'active:bool']
  products: ['ID:int', 'title:str', 'price:int', 'available:bool']

3. drop_table — Удаление таблицы
Синтаксис:

drop_table <имя_таблицы>

Описание:
Удаляет указанную таблицу и все её данные из базы данных. Операция необратима!

Пример:

drop_table users

Результат:

Таблица "users" удалена

4. insert — Добавление записи
Синтаксис:

insert into <таблица> values (<значение1>, <значение2>, ...)

Описание:
Добавляет новую запись в таблицу. ID назначается автоматически.

Примеры:

insert into users values ("Sergei", 28, true)
insert into users values ("Anna", 25, false)
insert into products values ("Laptop", 50000, true)

Результат:

Запись с ID=1 успешно добавлена в таблицу "users".

Типы значений:

Строки в кавычках: "Sergei", "Anna"
Числа без кавычек: 28, 25
Булевы значения: true, false
5. select — Выборка записей
Синтаксис:

select from <таблица> [where <столбец> = <значение>]

Описание:
Выбирает записи из таблицы. Можно использовать с условием WHERE или без него.

Примеры:

Выбрать все записи:

select from users

Результат:

{'ID': 1, 'name': 'Sergei', 'age': 28, 'active': True}
{'ID': 2, 'name': 'Anna', 'age': 25, 'active': False}

Выбрать с условием:

select from users where active = true
select from users where name = Sergei
select from users where age = 28

Результат:

{'ID': 1, 'name': 'Sergei', 'age': 28, 'active': True}

Если записей нет:

Записей не найдено.

6. update — Обновление записей
Синтаксис:

update <таблица> set <столбец> = <значение> [where <столбец> = <значение>]

Описание:
Обновляет значения в записях. Можно обновить все записи или только те, что соответствуют условию WHERE.

Примеры:

Обновить с условием:

update users set age = 29 where name = Sergei
update users set active = false where age = 25

Результат:

Обновлено записей: 1

Обновить все записи:

update users set active = true

Результат:

Обновлено записей: 3

7. delete — Удаление записей
Синтаксис:

delete from <таблица> [where <столбец> = <значение>]

Описание:
Удаляет записи из таблицы. Можно удалить все записи или только те, что соответствуют условию WHERE.

Примеры:

Удалить с условием:

delete from users where name = Anna
delete from users where age = 25

Результат:

Удалено записей: 1

Удалить все записи:

delete from users

Результат:

Удалено записей: 3

8. help — Справка
Синтаксис:

help

Описание:
Показывает справочную информацию по всем доступным командам.

9. exit — Выход
Синтаксис:

exit

Описание:
Завершает работу с базой данных и выходит из программы.

Полный пример работы (CRUD операции)
$ make run
***
Добро пожаловать в Primitive DB!
Введите 'help' для справки
Введите команду: create_table users name:str age:int active:bool
Таблица "users" создана
Введите команду: insert into users values ("Sergei", 28, true)
Запись с ID=1 успешно добавлена в таблицу "users".
Введите команду: insert into users values ("Anna", 25, false)
Запись с ID=2 успешно добавлена в таблицу "users".
Введите команду: insert into users values ("Ivan", 30, true)
Запись с ID=3 успешно добавлена в таблицу "users".
Введите команду: select from users
{'ID': 1, 'name': 'Sergei', 'age': 28, 'active': True}
{'ID': 2, 'name': 'Anna', 'age': 25, 'active': False}
{'ID': 3, 'name': 'Ivan', 'age': 30, 'active': True}
Введите команду: select from users where active = true
{'ID': 1, 'name': 'Sergei', 'age': 28, 'active': True}
{'ID': 3, 'name': 'Ivan', 'age': 30, 'active': True}
Введите команду: update users set age = 29 where name = Sergei
Обновлено записей: 1
Введите команду: select from users where name = Sergei
{'ID': 1, 'name': 'Sergei', 'age': 29, 'active': True}
Введите команду: delete from users where name = Anna
Удалено записей: 1
Введите команду: select from users
{'ID': 1, 'name': 'Sergei', 'age': 29, 'active': True}
{'ID': 3, 'name': 'Ivan', 'age': 30, 'active': True}
Введите команду: exit
Выход из программы...

Разработка
Команды Makefile
# Установка зависимостей
make install
# Запуск приложения
make run
# Сборка пакета
make build
# Публикация (dry-run)
make publish
# Установка собранного пакета
make package-install
# Линтинг кода
make lint

Структура проекта
project-2_kolesnik_matvey_m25-555/
├── src/
│   └── primitive_db/
│       ├── __init__.py      # Инициализация пакета
│       ├── main.py          # Точка входа
│       ├── engine.py        # Главный цикл и обработка команд
│       ├── core.py          # CRUD операции и валидация
│       ├── parser.py        # Парсинг SQL-подобных команд
│       └── utils.py         # Работа с JSON (загрузка/сохранение)
├── data/                    # Директория с данными таблиц (создаётся автоматически)
│   └── *.json              # Файлы данных для каждой таблицы
├── pyproject.toml           # Конфигурация Poetry
├── Makefile                 # Автоматизация команд
├── README.md                # Документация
├── .gitignore               # Игнорируемые файлы
└── db_meta.json             # Файл метаданных (создаётся автоматически)

Описание модулей
utils.py — функции для загрузки и сохранения JSON-данных (load_metadata, save_metadata, load_table_data, save_table_data)
core.py — бизнес-логика CRUD операций (create_table, drop_table, insert, select, update, delete, validate_value)
parser.py — парсинг SQL-подобных команд (parse_values, parse_where_clause, parse_set_clause)
engine.py — интерактивный цикл, обработка пользовательского ввода с помощью match case
main.py — точка входа в приложение
Технологии
Python 3.10+ — язык программирования
Poetry — управление зависимостями и сборка пакета
prompt — библиотека для интерактивного ввода данных
shlex — парсинг командной строки с поддержкой кавычек
json — хранение метаданных и данных таблиц
os — работа с файловой системой
Возможности
Cоздание таблиц с типизированными столбцами
Удаление таблиц вместе с данными
Добавление записей с автоматическим ID
Выборка записей (все или по условию WHERE)
Обновление записей (все или по условию WHERE)
Удаление записей (все или по условию WHERE)
Валидация типов данных (int, str, bool)
Персистентность данных в JSON файлах
SQL-подобный синтаксис команд

Демострация

[![asciicast](https://asciinema.org/a/oNiXAXIqtcLWYLJLiPbT1DTqH)]

*Полная демонстрация всех CRUD операций Primitive DB*

Автор
Колесник Матвей, группа М25-555

Лицензия
MIT
