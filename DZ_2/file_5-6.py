from datetime import date

class MyClass1:
    people_list = []
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age
        MyClass1.people_list.append(self)

    @classmethod
    def from_birth_year(cls, surname, name, birthyear):
        return cls(surname, name, date.today().year - birthyear)

    def print_info(self):
        print(self.surname + " " + self.name + "'s age is: " + str(self.age))


    @staticmethod
    def majority(land, age):
        if (land == "USA" and age < 21) or (land == "UA" and age < 18):
            print(f"In {land}: Not an adult")
        else:
            print(f"In {land}: Adult")

    @classmethod
    def count_adult(cls):
        ua = 0
        usa = 0
        for people in cls.people_list:
            if people.age >= 21:
                usa += 1
            if people.age >= 18:
                ua += 1
        return f"In UA {ua} is adult, in USA {usa} is adult"

class MyClass2(MyClass1):
    color = 'White'


m_per1 = MyClass1('Ivanenko', 'Ivan', 19)
m_per1.print_info()

m_per2 = MyClass1.from_birth_year('Dovzhenko', 'Bogdan',  2000)
m_per2.print_info()

m_per3 = MyClass2.from_birth_year('Sydorchuk', 'Petro', 2010)
m_per3.print_info()

m_per4 = MyClass2.from_birth_year('Makuschenko', 'Dmytro', 2001)
m_per4.print_info()

MyClass2.majority("USA", m_per1.age)
MyClass2.majority("USA", m_per2.age)
MyClass1.majority("UA", m_per3.age)
MyClass1.majority("UA", m_per4.age)

print(MyClass1.count_adult())