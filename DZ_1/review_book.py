"""Клас виводе інфо книги та відгуки до неї"""

class BookReview:
    def __init__(self, title, author, year, genre, reviews= None):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        if self.reviews is None:
            self.reviews = []
        else:
            self.reviews = reviews

    def __str__(self):
        return f"Book({self.title}, {self.author}, {self.year}, {self.genre}. Відгуки: {self.reviews})"

book_1 = BookReview("Гаррі Поттер і Філософський камінь", "Джоан Роулинг", 2001, "Фентезі")
book_2 = BookReview("1984", "Джордж Оруелл", 1949, "Антиутопія")
book_3 = BookReview("Володар перснів", "Дж. Р. Р. Толкін", 1954, "Фентезі")
book_4 = BookReview("Сяйво", "Стівен Кінг", 1977, "Жахи")

book_1.reviews = [
    "Найкраща казка дитинства, перечитую щороку!",
    "Фільм гарний, але в книзі більше деталей.",
    "Дуже атмосферно, Гоґвортс як рідний дім."
]
book_2.reviews = [
    "Страшно, бо дуже схоже на сьогодення.",
    "Книга важка психологічно, але корисна.",
    "Великий Брат стежить за тобою..."
]
book_3.reviews = [
    "Це база! Батько всього фентезі.",
    "Трохи важко читати описи природи, але сюжет епічний.",
    "Фродо молодець, але Сем — справжній герой."
]
book_4.reviews = [
    "Кінг — майстер жахів, читала з увімкненим світлом.",
    "Фільм Кубрика і книга — це дві різні історії.",
    "Дуже добре показано божевілля людини."
]

for book in [book_1, book_2, book_3, book_4]:
    print(f"Книга:\n{book.title}, {book.author}, {book.year}, {book.genre}")
    print(f"Відгуки:")
    for review in book.reviews:
        print(f" - {review}")
    print("-" * 5)