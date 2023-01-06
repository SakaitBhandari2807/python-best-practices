from composition.Book import Book


class BookShelf:
    def __init__(self, capacity):
        self.capacity = capacity
        self.quantity = 0
        self.books = []

    def __str__(self):
        return f"BookShelf with {self.quantity} books."

    def add_book(self, book: Book):
        if self.capacity > 0:
            self.books.append(book)
            self.capacity -= 1
            self.quantity += 1
        else:
            raise "BookShelf capacity full"

    def add_books(self, *books):
        for book in books:
            if self.capacity > 0:
                self.books.append(book)
                self.capacity -= 1
                self.quantity += 1
            else:
                raise "BookShelf capacity full"

