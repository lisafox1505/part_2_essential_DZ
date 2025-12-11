"""Клас """
class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.year}', '{self.genre}')"
    def __str__(self):
        return f"Book({self.title}, {self.author}, {self.year}, {self.genre})"

book_1 = Book("Гаррі Поттер і Філософський камінь", "Джоан Роулинг", 2001, "Фентезі")
book_2 = Book("1984", "Джордж Оруелл", 1949, "Антиутопія")
book_3 = Book("Володар перснів", "Дж. Р. Р. Толкін", 1954, "Фентезі")
book_4 = Book("Сяйво", "Стівен Кінг", 1977, "Жахи")

for book in [book_1, book_2, book_3, book_4]:
    print(book)
    print([book])
    print("*" * 10)