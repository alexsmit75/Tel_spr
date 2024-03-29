Реализовать телефонный справочник со следующими возможностями:
1.                   Вывод постранично записей из справочника на экран
2.                   Добавление новой записи в справочник
3.                   Возможность редактирования записей в справочнике
4.                   Поиск записей по одной или нескольким характеристикам
Требования к программе:
1.                   Реализация интерфейса через консоль (без веб- или графического интерфейса)
2.                   Хранение данных должно быть организовано в виде текстового файла, формат которого придумывает сам программист
3.                   В справочнике хранится следующая информация: фамилия, имя, отчество, название организации, телефон рабочий, телефон личный (сотовый)
Плюсом будет:
1.                   аннотирование функций и переменных
2.                   документирование функций
3.                   подробно описанный функционал программы
4.                   размещение готовой программы и примера файла с данными на github

Документирование функций
phonebook.py

Этот модуль реализует программу телефонного справочника с базовыми операциями.

"""

import os
from typing import List

def print_menu() -> None:
    """Выводит меню программы на экран."""
    ...

def display_records(filename: str, page_size: int = 5) -> None:
    """Выводит записи из справочника на экран постранично.

    Args:
        filename (str): Имя файла со справочником.
        page_size (int, optional): Количество записей на одной странице. По умолчанию 5.
    """
    ...

def add_record(filename: str) -> None:
    """Добавляет новую запись в справочник.

    Args:
        filename (str): Имя файла со справочником.
    """
    ...

def edit_record(filename: str) -> None:
    """Редактирует существующую запись в справочнике.

    Args:
        filename (str): Имя файла со справочником.
    """
    ...

def search_records(filename: str) -> None:
    """Ищет записи в справочнике по заданным характеристикам.

    Args:
        filename (str): Имя файла со справочником.
    """
    ...

def main() -> None:
    """Основная функция программы."""
    ...

if __name__ == "__main__":
    main()
