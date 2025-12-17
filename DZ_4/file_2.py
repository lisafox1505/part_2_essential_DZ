class Calculation:
    def __init__(self, arg_1, arg_2):
        self.arg_1 = arg_1
        self.arg_2 = arg_2

    def suma(self):
        if self.arg_2 < 0:
            return f"{self.arg_1}{self.arg_2} = {self.arg_1 + self.arg_2}"
        else:
            return f"{self.arg_1}+{self.arg_2} = {self.arg_1 + self.arg_2}"

    def subtraction(self):
        if self.arg_2 < 0:
            return f"{self.arg_1}+{abs(self.arg_2)} = {self.arg_1 - self.arg_2}"
        else:
            return f"{self.arg_1}-{self.arg_2} = {self.arg_1 - self.arg_2}"

    def multiplication(self):
        return f"{self.arg_1}*{self.arg_2} = {self.arg_1 * self.arg_2}"

    def division (self):
        try:
            return f"{self.arg_1}/{self.arg_2} = {self.arg_1 / self.arg_2}"
        except ZeroDivisionError:
            return "На ноль ділити не можна!"

    def exponentiation (self):
        try:
            return f"Число {self.arg_1} в {self.arg_2} ступені: {self.arg_1 ** self.arg_2}"
        except ZeroDivisionError:
            return "Не можна возводити 0 у від'ємну ступінь"

while True:
    actions_list = ["+", "-", "*", "/", "**"]
    action = input(f"Введіть бажану дію: {", ".join(actions_list)} або off щоб вийти:\n").strip().lower()
    if action == "off":
        break
    if action in actions_list:
        try:
            x = float(input("Введіть число 1:\n"))
            y = float(input("Введіть число 2:\n"))
            result = Calculation(x, y)
        except ValueError:
            print("Можна вводити тільки число!")
        else:
            match action:
                case "+":
                    print(result.suma())
                case "-":
                    print(result.subtraction())
                case "*":
                    print(result.multiplication())
                case "/":
                    print(result.division())
                case "**":
                    print(result.exponentiation())
    else:
        print("Такої дії не існує")