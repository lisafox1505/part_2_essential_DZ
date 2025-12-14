class GrafObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, wight, height):
        self.weight = wight
        self.height = height

class Clickable:
    def on_click(self):
        print("Клік мишкою!")

class Button(GrafObject, Rectangle, Clickable):
    def __init__(self, x, y, wight, height, color_button):
        GrafObject.__init__(self, x, y)
        Rectangle.__init__(self, wight, height)
        self.color_button = color_button
        print(f"Створено кнопку {self.color_button} кольору. Розмір {wight}/{height}. Координати {x}, {y}")
button = Button(100, 100, 20, 70, "червоного")
button.on_click()

