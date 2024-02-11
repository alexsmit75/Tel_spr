import os
from typing import List

# Функция для вывода меню
def print_menu() -> None:
    """Выводит меню программы на экран."""
    print("Телефонный справочник")
    print("1. Вывести записи")
    print("2. Добавить новую запись")
    print("3. Редактировать запись")
    print("4. Поиск записей")
    print("5. Выход")

# Функция для вывода записей из справочника постранично
def display_records(filename: str, page_size: int = 5) -> None:
    """Выводит записи из справочника на экран постранично.

    Args:
        filename (str): Имя файла со справочником.
        page_size (int, optional): Количество записей на одной странице. По умолчанию 5.
    """
    with open(filename, 'r') as file:
        records = file.readlines()
        num_pages = (len(records) + page_size - 1) // page_size
        for page in range(num_pages):
            print("\nСтраница", page + 1)
            start_index = page * page_size
            end_index = min(start_index + page_size, len(records))
            for i in range(start_index, end_index):
                print(records[i].strip())

# Функция для добавления новой записи в справочник
def add_record(filename: str) -> None:
    """Добавляет новую запись в справочник.

    Args:
        filename (str): Имя файла со справочником.
    """
    with open(filename, 'a') as file:
        surname: str = input("Введите фамилию: ")
        if not surname:
            print("Ошибка: Фамилия не может быть пустой.")
            return
        name: str = input("Введите имя: ")
        if not name:
            print("Ошибка: Имя не может быть пустым.")
            return
        patronymic: str = input("Введите отчество: ")
        if not patronymic:
            print("Ошибка: Отчество не может быть пустым.")
            return
        organization: str = input("Введите название организации: ")
        if not organization:
            print("Ошибка: Название организации не может быть пустым.")
            return
        work_phone: str = input("Введите рабочий телефон: ")
        if not work_phone:
            print("Ошибка: Рабочий телефон не может быть пустым.")
            return
        personal_phone: str = input("Введите личный телефон (сотовый): ")
        if not personal_phone:
            print("Ошибка: Личный телефон не может быть пустым.")
            return
        file.write(f"{surname}, {name}, {patronymic}, {organization}, {work_phone}, {personal_phone}\n")

# Функция для редактирования записи в справочнике
def edit_record(filename: str) -> None:
    """Редактирует существующую запись в справочнике.

    Args:
        filename (str): Имя файла со справочником.
    """
    with open(filename, 'r') as file:
        records: List[str] = file.readlines()

    if not records:
        print("Справочник пустой. Нечего редактировать.")
        return

    while True:
        try:
            index_input: str = input("Введите номер записи, которую хотите отредактировать (или оставьте пустым для отмены): ").strip()
            if not index_input:
                print("Редактирование отменено.")
                return
            index: int = int(index_input) - 1
            if 0 <= index < len(records):
                break
            else:
                print("Неверный номер записи. Попробуйте снова.")
        except ValueError:
            print("Неверный формат номера записи. Попробуйте снова.")

    while True:
        new_record: str = input("Введите новую информацию в формате 'Фамилия, Имя, Отчество, Организация, Рабочий телефон, Личный телефон' (или оставьте пустым для выхода): ").strip()
        if not new_record:
            print("Редактирование отменено.")
            return
        if new_record.count(',') != 5:
            print("Ошибка: Неправильный формат записи. Попробуйте снова.")
        else:
            records[index] = new_record + '\n'
            with open(filename, 'w') as file:
                file.writelines(records)
            print("Запись успешно отредактирована.")
            return

# Функция для поиска записей в справочнике по заданным характеристикам
def search_records(filename: str) -> None:
    """Ищет записи в справочнике по заданным характеристикам.

    Args:
        filename (str): Имя файла со справочником.
    """
    search_criteria: List[str] = input("Введите критерии поиска (разделите пробелом): ").split()
    with open(filename, 'r') as file:
        for line in file:
            record: List[str] = line.strip().split(', ')
            if all(criteria.lower() in value.lower() for criteria, value in zip(search_criteria, record)):
                print(', '.join(record))

# Основная функция программы
def main() -> None:
    """Основная функция программы."""
    filename: str = "phonebook.txt"
    if not os.path.exists(filename):
        with open(filename, 'w'):
            pass
    while True:
        print_menu()
        choice: str = input("Выберите действие: ")
        if choice == '1':
            display_records(filename)
        elif choice == '2':
            add_record(filename)
        elif choice == '3':
            edit_record(filename)
        elif choice == '4':
            search_records(filename)
        elif choice == '5':
            print("До свидания!")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
