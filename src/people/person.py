from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self,name,email):
        self.name = name
        self.email = email

    @property
    def _name(self):
        return self.name
    @property
    def _email(self):
        return self.email
    
