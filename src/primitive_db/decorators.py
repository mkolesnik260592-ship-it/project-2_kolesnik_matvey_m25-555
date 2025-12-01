"""Декораторы для Primitive DB."""
import time
from functools import wraps


def handle_db_errors(func):
    """Декоратор для обработки ошибок базы данных"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            print(
                "Ошибка: Файл данных не найден"
                "Возможно, база данных не инициализирована."
            )
            return None
        except KeyError as e:
            print(f"Ошибка: Таблица или столбец {e} не найден.")
            return None
        except ValueError as e:
            print(f"Ошибка валидации: {e}")
            return None
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")
            return None
    return wrapper

def confirm_action(action_name):
    """Декоратор-фабрика для подтверждения опасных операций."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            ans = input(f'Вы уверены, что хотите выполнить "{action_name}" [y/n]: ')
            if ans.lower() == 'y':
                return func(*args, **kwargs)
            else:
                print("Операция отменена.")
                return args[0] if args else None
        return wrapper
    return decorator

def log_time(func):
    """Декоратор для замера времени выполнения функции."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.monotonic()
        result = func(*args, **kwargs)
        end_time = time.monotonic()
        work_time = end_time - start_time
        print(f'Функция {func.__name__} выполнилась за {work_time:.3f} секунд.')
        return result
    return wrapper

def create_cacher():
    """Создаёт функцию кэширования с замыканием."""
    # 1. Создайте пустой словарь cache = {}
    cache = {}
    def cache_result(key, value_func):
        """Кэширует результат вызова функции."""
        # 2. Проверьте, есть ли key в cache
        if key in cache:
            print(f'[CACHE] Результат найден для ключа: {key}')
            return cache[key]
        else:
            print(f'[CACHE] Вычисление результата для ключа: {key}')
            cache[key] = value_func()
            return cache[key]
    return cache_result
