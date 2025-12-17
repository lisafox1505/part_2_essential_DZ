class Employee:

    def __init__(self, name: str, surname: str, department: str, year_start: int):
        if not isinstance(name, str) or not isinstance(surname, str) or not isinstance(department, str):
            raise TypeError("Ім'я, прізвище та відділ повинні бути string")

        if not isinstance(year_start, int):
            raise TypeError("Рік повинен бути integer")

        if len(name) == 0 or len(surname) == 0 or len(department) == 0 or not year_start:
            raise ValueError("Данні не повинні бути порожніми")

        if year_start < 1950 or year_start > 2025:
            raise ValueError("Рік повинен бути між 1950 та 2025")

        self.name = name
        self.surname = surname
        self.department = department
        self.year_start = year_start

    def __str__(self):
        return f"{self.name} {self.surname} - {self.department}, {self.year_start}"

employees = []
while True:
    input_data = input("Для вихода натисніть Enter. Введіть дані співробітника через кому: ").strip().lower().capitalize()
    if not input_data:
        break
    input_data = input_data.split(",")
    if len(input_data) != 4:
        print("Данні введені не вірно!")
        continue
    try:
        name_emp = input_data[0].strip().lower().capitalize()
        surname_emp = input_data[1].strip().lower().capitalize()
        depart = input_data[2].strip().capitalize()
        year = int(input_data[3].strip())
        employees.append(Employee(name_emp, surname_emp, depart, year))
    except ValueError as e:
        print(e)
        continue

while True:
    try:
        desired_year = int(input("Введіть рік для фільтрації: "))
        if desired_year < 1950 or desired_year > 2025:
            print("Рік повинен бути між 1950 та 2025")
            continue
        for i in employees:
            if i.year_start > desired_year:
                print(i)
        break
    except ValueError:
        print("Рік введен не вірно!")
        continue
