from python_oop.classes_and_objects.exercise.project_lib import user


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}  # {usernames: {book names: days to return}})

    def add_user(self, user):
        if user not in self.user_records:
            self.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user):
        if user not in self.user_records:
            return "We could not find such user to remove!"
        self.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str):
        if not user.user_id and not user_id == user.user_id:
            return f"rThere is no user with id = {user_id}!"
        if user.user_id and user_id == user.user_id and new_username == user.username:
            return "Please check again the provided username - it should be different than the username used so far"
        User.username = new_username
        self.rented_books[new_username] = self.rented_books[user.username]
        del self.rented_books[user.username]
        return f"Username successfully changed to: {new_username} for userid: {user_id}"
