from .library_item import LibraryItem

class Book(LibraryItem):
    def __init__(self, title, author, isbn, copies=1, genre=None):
        super().__init__(title, author, isbn, copies)
        self.genre = genre
    @classmethod
    def get_type(cls):
        return "Book"
    
    def __str__(self):
        return f"\nISBN: {self.isbn}\nTitle: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}\nCopies: {self.copies}\nType: {self.get_type()}\n"
