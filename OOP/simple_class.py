class Book:
    def __init__(self):
        self.name = None
        self.auther = None
        self.description = None

    def __str__(self):
        return f'Name:{self.name}\nAuther:{self.auther}\nDescription:{self.description}\n'

    def create_book(self, name, auther, description):
        self.name = name
        self.auther = auther
        self.description = description
        return self

    def get_book(self):
        return self

    def update_book(self, name=None, auther=None, description=None):
        if name is not None:
            self.name = name
        if auther is not None:
            self.auther = auther
        if description is not None:
            self.description = description


class Books:
    def __init__(self):
        self.books = []

    def __iter__(self):
        pass

    def __getitem__(self, item):
        return self.books[item]

    def __str__(self):
        string = ''
        for i in self.books:
            string += i.__str__() + '\n'
        return string

    def append(self, book):
        result = isinstance(book, Book)
        if result:
            self.books.append(book)
        else:
            print("Not a book")

    def pop(self):
        return self.books.pop()

    def remove(self, book: Book):
        return self.books.remove(book)


if __name__ == '__main__':
    books = Books()
    for i in range(10):
        books.append(
            book=Book().create_book(
                name=f"Name {i}",
                auther=f"Max {i}",
                description="Test Book"
            )
        )
    print(books)
    print(books.pop())
    print(books.remove(books[0]))
    print(books)
