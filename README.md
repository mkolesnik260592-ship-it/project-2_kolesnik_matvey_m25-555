# Primitive DB

Простая интерактивная база данных на Python с командной строкой для управления таблицами.

## Описание

Primitive DB — это учебный проект CLI-приложения для управления таблицами, демонстрирующий:

- Создание Python-пакетов с Poetry
- Интерактивный CLI с библиотекой `prompt`
- Работу с JSON для хранения метаданных
- Организацию кода в модули (OOP, парсинг команд)
- Публикацию пакетов

## Установка

### Требовани

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
database

Управление таблицами
Список команд
Команда #Описание
create_table <имя> <столбец:тип> ... #Создать новую таблицу
list_tables #Показать все таблицы
drop_table <имя> #Удалить таблицу
help #Показать справку
exit #Выйти из программы

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

# Создать таблицу пользователей
create_table users name:str age:int
# Создать таблицу товаров
create_table products title:str price:int available:bool
# Создать таблицу заказов
create_table orders user_id:int product_id:int quantity:int

Успешный результат:

Таблица "users" создана

Ошибки:

Таблица уже существует:
create_table users email:str
Ошибка: таблица "users" уже существует

Недопустимый тип данных:
create_table test price:float
Ошибка: недопустимый тип "float"

Недостаточно аргументов:
create_table users
Ошибка: недостаточно аргументов
Использование: create_table <имя> <столбец:тип> ...

2. list_tables — Список таблиц
Синтаксис:

list_tables

Описание:
Показывает список всех созданных таблиц с их структурой (названия столбцов и типы).

Примеры:

list_tables

Результат:

Список таблиц:
  users: ['ID:int', 'name:str', 'age:int']
  products: ['ID:int', 'title:str', 'price:int', 'available:bool']
  orders: ['ID:int', 'user_id:int', 'product_id:int', 'quantity:int']

Если таблиц нет:

Нет таблиц

3. drop_table — Удаление таблицы
Синтаксис:

drop_table <имя_таблицы>

Описание:
Удаляет указанную таблицу из базы данных. Операция необратима!

Примеры:

# Удалить таблицу users
drop_table users
# Удалить таблицу products
drop_table products

Успешный результат:

Таблица "users" удалена

Ошибки:

Таблица не существует:
drop_table nonexistent
Ошибка: таблица "nonexistent" не существует

Не указано имя таблицы:

drop_table
Ошибка: укажите имя таблицы
Использование: drop_table <имя>

4. help — Справка
Синтаксис:

help

Описание:
Показывает справочную информацию по всем доступным командам.

Результат:

***Процесс работы с таблицей***
Функции:
<command> create_table <имя_таблицы> <столбец1:тип> .. - создать таблицу
<command> list_tables - показать список всех таблиц
<command> drop_table <имя_таблицы> - удалить таблицу
Общие команды:
<command> exit - выход из программы
<command> help - справочная информация

5. exit — Выход
Синтаксис:

exit

Описание:
Завершает работу с базой данных и выходит из программы.

Результат:

Выход из программы...

Полный пример работы
$ make run
***
Добро пожаловать в Primitive DB!
Введите 'help' для справки
Введите команду: create_table users name:str age:int
Таблица "users" создана
Введите команду: create_table products title:str price:int available:bool
Таблица "products" создана
Введите команду: list_tables
Список таблиц:
  users: ['ID:int', 'name:str', 'age:int']
  products: ['ID:int', 'title:str', 'price:int', 'available:bool']
Введите команду: create_table users email:str
Ошибка: таблица "users" уже существует
Введите команду: drop_table products
Таблица "products" удалена
Введите команду: list_tables
Список таблиц:
  users: ['ID:int', 'name:str', 'age:int']
Введите команду: drop_table nonexistent
Ошибка: таблица "nonexistent" не существует
Введите команду: help
***Процесс работы с таблицей***
Функции:
<command> create_table <имя_таблицы> <столбец1:тип> .. - создать таблицу
<command> list_tables - показать список всех таблиц
<command> drop_table <имя_таблицы> - удалить таблицу
Общие команды:
<command> exit - выход из программы
<command> help - справочная информация
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
│       ├── engine.py        # Игровой цикл и обработка команд
│       ├── core.py          # Логика создания/удаления таблиц
│       └── utils.py         # Работа с JSON (загрузка/сохранение)
├── pyproject.toml           # Конфигурация Poetry
├── Makefile                 # Автоматизация команд
├── README.md                # Документация
├── .gitignore               # Игнорируемые файлы
└── db_meta.json             # Файл метаданных (создаётся автоматически)

Описание модулей
utils.py — функции для загрузки и сохранения JSON-метаданных (load_metadata, save_metadata)
core.py — бизнес-логика создания и удаления таблиц (create_table, drop_table)
engine.py — интерактивный цикл, парсинг команд с помощью shlex, обработка пользовательского ввода
main.py — точка входа в приложение
Технологии
Python 3.10+ — язык программирования
Poetry — управление зависимостями и сборка пакета
prompt — библиотека для интерактивного ввода данных
shlex — парсинг командной строки с поддержкой кавычек
json — хранение метаданных таблиц

Демонстрация
https://asciinema.org/connect/5d8eff4f-cd97-42cd-9343-55f0d1ca1c65
Автор
Колесник Матвей, группа М25-555

Лицензия
MIT
