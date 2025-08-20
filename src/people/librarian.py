from .person import Person

class Librarian(Person):
    def __init__(self, name, email, admin_id, library):
        super().__init__(name, email)
        self.admin_id = admin_id
        self.library = library

    def add_item(self, item):
        self.library.add_item(item)

    def remove_item(self, isbn):
        self.library.remove_item(isbn)

    def update_item(self, isbn):
        self.library.update_item(isbn)

    def view_all_items(self):
        return self.library.list_items()

    def view_all_transactions(self):
        self.library.list_transactions()
    def view_item(self,isbn):
        print(self.library.get_item(isbn))
    def __str__(self):
        return f"Librarian[{self.admin_id}] {self.name}, Email: {self.email}, Library: {self.library.name}"
