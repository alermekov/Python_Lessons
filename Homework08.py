import os

class Record:
    def __init__(self, surname, name, patronymic, phone):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone = phone

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic} - {self.phone}"

class PhoneBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        for r in self.records:
            if r.phone == record.phone:
                print("Данная запись уже существует!")
                return
        self.records.append(record)
        print("Запись успешно добавлена!")

    def remove_record(self, record):
        choice = input("Вы действительно хотите удалить эту запись? (y/n)")
        if choice.lower() == "y":
            self.records.remove(record)
            print("Запись успешно удалена!")
        else:
            print("Удаление отменено.")

    def edit_record(self, record):
        print("Введите новые данные для записи:")
        surname = input("Фамилия: ")
        name = input("Имя: ")
        patronymic = input("Отчество: ")
        phone = record.phone
        new_record = Record(surname, name, patronymic, phone)
        self.remove_record(record)
        self.add_record(new_record)

    def search_record(self, attr, value):
        results = []
        for r in self.records:
            if getattr(r, attr) == value:
                results.append(r)
        if len(results) > 0:
            print(f"Найдено {len(results)} записей:")
            for r in results:
                print(r)
        else:
            print("Записей не найдено.")

    def sort_records(self, attr):
        self.records.sort(key=lambda x: getattr(x, attr))

    def export_data(self, filename):
        with open(filename, "w") as f:
            for r in self.records:
                f.write(f"{r.surname},{r.name},{r.patronymic},{r.phone}\n")
        print("Данные успешно экспортированы!")

    def import_data(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                data = line.strip().split(",")
                record = Record(data[0], data[1], data[2], data[3])
                self.add_record(record)
        print("Данные успешно импортированы!")

phone_book = PhoneBook()

if os.path.isfile("phonebook.txt"):
    phone_book.import_data("phonebook.txt")

while True:
    print("\nВыберите действие:")
    print("1. Просмотреть записи")
    print("2. Добавить новую запись")
    print("3. Удалить запись")
    print("4. Изменить запись")
    print("5. Поиск записей")
    print("6. Сортировка записей")
    print("7. Экспорт данных")
    print("8. Выход")

    choice = input("Введите номер действия: ")

    if choice == "1":
        if len(phone_book.records) > 0:
            for r in phone_book.records:
                print(r)
        else:
            print("Записей нет.")

    elif choice == "2":
        surname = input("Фамилия: ")
        name = input("Имя: ")
        patronymic = input("Отчество: ")
        phone = input("Номер телефона: ")
        record = Record(surname, name, patronymic, phone)
        phone_book.add_record(record)

    elif choice == "3":
        phone = input("Введите номер телефона записи, которую нужно удалить: ")
        for r in phone_book.records:
            if r.phone == phone:
                phone_book.remove_record(r)
                break
        else:
            print("Запись не найдена.")

    elif choice == "4":
        phone = input("Введите номер телефона записи, которую нужно изменить: ")
        for r in phone_book.records:
            if r.phone == phone:
                phone_book.edit_record(r)
                break
        else:
            print("Запись не найдена.")

    elif choice == "5":
        attr = input("Введите характеристику для поиска (surname, name, patronymic, phone): ")
        value = input("Введите значение характеристики: ")
        phone_book.search_record(attr, value)

    elif choice == "6":
        attr = input("Введите характеристику для сортировки (surname, name): ")
        phone_book.sort_records(attr)

    elif choice == "7":
        phone_book.export_data("phonebook.txt")

    elif choice == "8":
        break

    else:
        print("Некорректный ввод. Попробуйте еще раз.")