from data_sport import sports_dict, coaches_dict, schedule_dict, prices_dict

class NotKeyFound(Exception):
    def __init__(self, message = "Тренер не знайден!"):
        self.message = message
        super().__init__(self.message)

def prity_string(data_dict):
    for key, value in data_dict.items():
        print(f"{key:15} - {value}")

while True:
    print("""\n    МЕНЮ СПОРТИВНОГО КОМПЛЕКСУ
    1 - Перелік видів спорту
    2 - Команда тренерів
    3 - Розклад тренувань
    4 - Вартість тренування
    5 - Пошук тренера по імені
    0 - Вихід
          """)
    try:
        choice = int(input("\nОберіть пункт меню: "))
        match choice:
            case 0:
                break
            case 1:
                prity_string(sports_dict)
            case 2:
                prity_string(coaches_dict)
            case 3:
                prity_string(schedule_dict)
            case 4:
                prity_string(prices_dict)
            case 5:
                coach_name = input("Введіть ім'я тренера: ").strip().lower().title()
                try:
                    if coach_name not in coaches_dict:
                        raise NotKeyFound
                    coach = coaches_dict[coach_name]
                    print(f"{coach_name} - {coach}")
                except NotKeyFound as e:
                    print(e)
    except ValueError:
        print("Невірний ввод")