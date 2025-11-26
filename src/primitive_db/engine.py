"""Движок для работы с Primitive DB."""

import prompt


def welcome():
    """Главная функция для запуска интерактивной оболочки."""
    print("***")
    print("<command> exit - выйти из программы")
    print("<command> help - справочная информация")

    while True:
        user_input = prompt.string("Введите команду: ")

        if user_input == "exit":
            print("Выход из программы...")
            break
        elif user_input == "help":
            print()
            print("<command> exit - выйти из программы")
            print("<command> help - справочная информация")
        else:
            print(f"Неизвестная команда: {user_input}")
            print("Введите 'help' для справки")
