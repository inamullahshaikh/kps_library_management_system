from .library_item import LibraryItem

class Journal(LibraryItem):
    def __init__(self, title, author, isbn, copies=1, volume=None):
        super().__init__(title, author, isbn, copies)
        self.volume = volume
    @classmethod
    def get_type(cls):
        return "Journal"
    def __str__(self):
        return f"\nISBN: {self.isbn}\nTitle: {self.title}\nAuthor: {self.author}\nVolume: {self.volume}\nCopies: {self.copies}\nType: {self.get_type()}\n"
