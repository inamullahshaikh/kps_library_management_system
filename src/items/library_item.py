from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title, author, isbn, copies=1):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._copies = copies

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if value and isinstance(value, str):
            self._title = value
        else:
            raise ValueError("Title must be a non-empty string")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if value and isinstance(value, str):
            self._author = value
        else:
            raise ValueError("Creator must be a non-empty string")

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        if value and isinstance(value, str):
            self._isbn = value
        else:
            raise ValueError("ISBN must be a valid string")

    @property
    def copies(self):
        return self._copies

    @copies.setter
    def copies(self, value):
        if isinstance(value, int) and value >= 0:
            self._copies = value
        else:
            raise ValueError("Copies must be a non-negative integer")

    def add_copy(self, count=1):
        self._copies += count

    def remove_copy(self, count=1):
        if self._copies >= count:
            self._copies -= count
        else:
            raise ValueError("Not enough copies to remove")

    def is_available(self):
        return "Yes" if self._copies > 0 else "No"
    @classmethod
    @abstractmethod
    def get_type(self):
        pass
    @abstractmethod
    def __str__(self):
        pass
