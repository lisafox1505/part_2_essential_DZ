#1
from random import uniform

with open('numbers.txt', 'w') as file:
    for _ in range(10000):
        print(f"{uniform(-500, 500):.2f}", file=file)

with open('numbers.txt', 'r') as file:
    result = sum(float(i.strip()) for i in file)
    print(f"{result:.2f}")

#2
import shelve

with shelve.open('my_storage') as dict_user:
    while True:
        print("Яку дію бажаєте виконати:\n1 - внести нові дані\n2 - знайти посиланя\n3 - подивитись усі ключі\n4 - видалити посилання\n5 - завершити")
        try:
            x = int(input("Ваш вибір: "))
            match x:
                case 1:
                    name = input("Введіть ім'я посилання: ")
                    if name not in dict_user:
                        url = input("Введіть посилання: ")
                        dict_user[name] = url
                        print(f"Дані додані")
                    else:
                        y = input("Такe ім'я вже існує. Перезаписати? Введіть Y або N: ")
                        y = y.strip().lower()
                        if y == "y":
                            url = input("Введіть посилання: ")
                            dict_user[name] = url
                            print(f"Дані змінені")
                        elif y == "n":
                            continue
                        else:
                            print("Невірний вибір")
                case 2:
                    key = input("Введіть ім'я посилання, яке шукаєте: ")
                    print(dict_user.get(key, "Такого ім'я не існує"))
                case 3:
                    print(list(dict_user.keys()))
                case 4:
                    key = input("Введіть ім'я посилання, яке хочете видалити: ")
                    if key not in dict_user:
                        print("Такого ім'я немає")
                        continue
                    del dict_user[key]
                    print("Посилання видалене")
                case 5:
                    break
                case _:
                    print("Невірний ввод")
        except ValueError:
            print("Невірний ввод")

#3
import json
import pickle

shop_goods = {
    "Ноутбук UltraBook X": {
        "price": 25000,
        "quantity": 5
    },
    "Бездротова мишка LogiTech": {
        "price": 500,
        "quantity": 20
    },
    "Механічна клавіатура Clicky": {
        "price": 1200,
        "quantity": 10
    },
    "Монітор 24'' ViewMaster": {
        "price": 8000,
        "quantity": 7
    },
    "Навушники SoundBass": {
        "price": 3500,
        "quantity": 15
    }
}

with open("shop_goods.pickle", 'wb') as file_1:
    pickle.dump(shop_goods, file_1)

with open("shop_goods.json", 'w', encoding='utf-8') as file_2:
    json.dump(shop_goods, file_2)