import shelve
from programm_logic import LinkShortService

with shelve.open('my_storage') as dict_user:
    obj_link = LinkShortService(dict_user)
    while True:
        print("Яку дію бажаєте виконати:\n1 - внести нові дані\n2 - знайти посиланя\n3 - подивитись усі ключі\n4 - видалити посилання\n5 - завершити")
        try:
            x = int(input("Ваш вибір: "))
            match x:
                case 1:
                    name = input("Введіть ім'я посилання: ")
                    if obj_link.check_key(name) is False:
                        url = input("Введіть посилання: ")
                        obj_link.add_new_data(name, url)
                        print(f"Дані додані")
                    else:
                        y = input("Такe ім'я вже існує. Перезаписати? Введіть Y або N: ")
                        if y == "y":
                            url = input("Введіть посилання: ")
                            obj_link.add_new_data(name, url)
                            print(f"Дані змінені")
                        elif y == "n":
                            continue
                        else:
                            print("Невірний вибір")
                case 2:
                    key = input("Введіть ім'я посилання, яке шукаєте: ")
                    print(obj_link.get_link(key))
                case 3:
                    print(obj_link.show_all_keys())
                case 4:
                    key = input("Введіть ім'я посилання, яке хочете видалити: ")
                    if obj_link.check_key(key) is False:
                        print("Такого ім'я немає")
                        continue
                    obj_link.del_link(key)
                    print("Посилання видалене")
                case 5:
                    break
                case _:
                    print("Невірний ввод")
        except ValueError:
            print("Невірний ввод")