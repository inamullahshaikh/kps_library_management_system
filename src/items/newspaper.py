from .library_item import LibraryItem
class Newspaper(LibraryItem):
    def __init__(self, title, author, isbn, copies=1, date=None):
        super().__init__(title, author, isbn, copies)
        self.date = date
    @classmethod
    def get_type(cls):
        return "Newspaper"
    def __str__(self):
        return f"\nISBN: {self.isbn}\nTitle: {self.title}\nAuthor: {self.author}\Date: {self.date}\nCopies: {self.copies}\nType: {self.get_type()}\n"
