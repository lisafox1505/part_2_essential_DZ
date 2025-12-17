import datetime

class ErrorYear(Exception):
    def __init__(self, year, message = "Рік на може бути менше 1900 року"):
        self.year = year
        self.message = message
        super().__init__(f"{message}: ви ввели {year}. Вам не може бути {datetime.datetime.now().year - year} років")

def user_birthday(birthday):
    birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d")
    if birthday.year <= 1900:
        raise ErrorYear(birthday.year)
    if birthday.year > datetime.datetime.now().year:
        raise ErrorYear(birthday.year, f"Це майбутнє. Зараз {datetime.datetime.now().year} рік")
    return f"Ваш день народження: {birthday.day}, місяць: {birthday.month}, рік: {birthday.year}"

try:
    user_data = input("Ведіть дату вашого народження в фоматі рррр-мм-дд: ").strip()
    print(user_birthday(user_data))
except ErrorYear as e:
    print(e)
except ValueError:
    print("Невірний формат дати")