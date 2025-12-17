from abc import ABC, abstractmethod
class Language(ABC):
    def __init__(self, language):
        self.language = language

    @abstractmethod
    def greeting(self):
        pass

class English(Language):
    def greeting(self):
        print(f"In {self.language.capitalize()}: Hello English")

class Germany(Language):
    def greeting(self):
       print(f"In {self.language.capitalize()}: Hallo Deutsch")

def hello_friend(obj):
    obj.greeting()

obj_1 = English("English")
obj_2 = Germany("Germany")

hello_friend(obj_1)
hello_friend(obj_2)