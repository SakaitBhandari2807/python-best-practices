from composition.BookShelf import BookShelf
from composition.Book import Book

if __name__ == "__main__":
    shelf = BookShelf(10)
    book1 = Book("Harry Potter", "J.K. Rowling")
    shelf.add_book(book1)

    print(shelf)
    print(book1)