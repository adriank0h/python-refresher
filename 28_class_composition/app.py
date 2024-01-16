class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."
    
shelf = BookShelf(300)

# print(shelf)

class Book:
    def __init__(self, name):
        self.name = name
    def __str__(self) -> str:
        return f"Book {self.name}"
    
book1 = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book1, book2)
print(book1)

#inheritance means a book is a bookshelf
#composition means a bookshelf has many books