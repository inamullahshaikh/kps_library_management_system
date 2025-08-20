from .library_item import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, title, author, isbn, copies=1, issue=None):
        super().__init__(title, author, isbn, copies)
        self.issue = issue
    @classmethod
    def get_type(cls):
        return "Magazine"
    def __str__(self):
        return f"\nISBN: {self.isbn}\nTitle: {self.title}\nAuthor: {self.author}\nIssue: {self.issue}\nCopies: {self.copies}\nType: {self.get_type()}\n"
