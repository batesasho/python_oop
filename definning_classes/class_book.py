class Book:
    def __init__(self, name: str, author: str, pages: int):
        self.pages = pages
        self.name = name
        self.author = author


book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)
