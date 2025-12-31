import inspect

class Contact:
    def __init__(self, surname, name, age, mob_phone, email):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def get_contact(self):
        print(f"{self.surname} {self.name}. Number: {self.mob_phone}. Email: {self.email}")

    def sent_message(self):
        print(f"Повідомлення для {self.surname} {self.name} выдправлене")

class UpdateContact(Contact):
    def __init__(self, surname, name, age, mob_phone, email, job):
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    def get_message(self):
        print(f"Отримано повідомлення від {self.surname} {self.name}.")


obj1 = UpdateContact("Shevchenko", "Andriy", 35, 380501112233, "andriy.shev@gmail.com", "Project Manager")
obj2 = UpdateContact("Kovalenko", "Oksana", 28, 380972223344, "koval.oksana@ukr.net", "UI/UX Designer")
obj3 = UpdateContact("Bondar", "Ihor", 42, 380633334455, "ihor.bondar@tech.com", "Python Developer")

# print(obj1.__dict__)
# print(obj2.__class__.__base__)
# print(obj3.__class__.__bases__)

"""Використовуючи код з завдання 2, використати функції hasattr(), getattr(), setattr(), delattr(). 
Застосувати ці функції до кожного з атрибутів класів, подивитися до чого це призводить"""

# key = input("Що саме змінити?: ")
# if hasattr(obj2, key):
#     action = input("Змінити чи видалити?: ").strip().lower()
#     if action == "змінити":
#         value = input("Введіть нове значення: ")
#         setattr(obj2, key, value)
#         print(getattr(obj2, key, 0))
#     elif action == "видалити":
#         delattr(obj2, key)
#         print(getattr(obj2, key, 0))
#     else:
#         print("Невірний ввод")
# else:
#     print("Такого значення не існує")

"""
Використовуючи код з завдання 2, створити 2 екземпляри обох класів. Використати функції isinstance() – для перевірки 
екземплярів класу (за яким класом створені) та issubclass() – для перевірки і визначення класу-нащадка."""

obj4 = Contact("Tkachenko", "Mariya", 31, 380734445566, "mariya.t@finance.ua")
obj5 = Contact("Melnyk", "Serhiy", 24, "+380665556677", "s.melnyk@start.up")

# print(isinstance(obj4, Contact))
# print(isinstance(obj5, UpdateContact))
# print(isinstance(obj2, Contact))
# print(isinstance(obj3, UpdateContact))
# print(issubclass(Contact, UpdateContact))
# print(issubclass(UpdateContact, Contact))

"""
Використовуючи код завдання 2 надрукуйте у терміналі інформацію, яка міститься у класах Contact та UpdateContact та їх екземплярах. 
Видаліть атрибут job, і знову надрукуйте стан класів та їх екземплярів. Порівняйте їх. Зробіть відповідні висновки.
"""
# print(f"Стан батьківського класу {Contact.__name__} та його екземпляру:")
# print(Contact.__dict__)
# print(obj4.__dict__)
# print(f"Стан наслідуючого класу {UpdateContact.__name__} та його екземпляру до видалення 'job':")
# print(UpdateContact.__dict__)
# print(obj3.__dict__)
# print("-"*20)
# print(f"Стан після видалення 'job':")
# delattr(obj3, "job")
# print(f"Стан батьківського класу {Contact.__name__} та його екземпляру:")
# print(Contact.__dict__)
# print(obj4.__dict__)
# print(f"Стан наслідуючого класу {UpdateContact.__name__} та його екземпляру:")
# print(UpdateContact.__dict__)
# print(obj3.__dict__)

"""
Використовуючи код завдання 2 надрукуйте у терміналі всі методи, які містяться у класі Contact та UpdateContact.
"""
for k, v in Contact.__dict__.items():
    if inspect.isfunction(v):
        print(f"{k}: {v}")
for k, v in UpdateContact.__dict__.items():
    if inspect.isfunction(v):
        print(f"{k}: {v}")



