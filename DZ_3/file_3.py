class Temp:
    def __init__(self, count=0):
        self.__temperature_celsius = count

    @property
    def celsius(self):
        return self.__temperature_celsius

    @celsius.setter
    def celsius(self, value):
        self.__temperature_celsius = value

    @property
    def fahrenheit(self):
        return (self.__temperature_celsius * 1.8) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.__temperature_celsius = (value - 32) * 5/9

c = Temp()
c.celsius = 25
c.fahrenheit = 71
print(c.celsius)
print(c.fahrenheit)

f = Temp()
f.celsius = 30
f.fahrenheit = 70
print(f.celsius)
print(f.fahrenheit)