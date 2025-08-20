from datetime import datetime

class Transaction:
    def __init__(self, admin, item, transaction_type):
        self.admin = admin
        self.item = item
        self.transaction_type = transaction_type
        self.date = datetime.now()

    def __str__(self):
        return f"[{self.date}] Librarian {self.admin.name} {self.transaction_type} {self.item._title}"
