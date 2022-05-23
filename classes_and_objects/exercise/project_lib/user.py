from python_oop.classes_and_objects.exercise.project_lib import library


class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library: library):
        if book_name in library.books_available[author]:
            self.books.append(book_name)
            library.books_available[author].remove(book_name)
            library.rented_books.setdefault(self.username, {})
            library.rented_books[self.username].update({book_name: days_to_return})
            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for user in library.rented_books:
            if book_name in library.rented_books[user]:
                return f'The book "{book_name}" is already rented and will be available in ' \
                       f'{library.rented_books[user][book_name]} days!'

    def return_book(self, author: str, book_name: str, library):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"
        self.books.remove(book_name)
        library.books_available[author].append(book_name)
        del library.rented_books[self.username][book_name]

    def info(self):
        return sorted(self.books, key = lambda x: x[0])

    def __str__(self):
        list_of_rented_books = self.info()
        return f"{user_id}, {username}, {list_of_rented_books}"
