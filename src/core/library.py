from .transactions import Transaction
from people.librarian import Librarian
from items.library_item import LibraryItem

def get_all_subclasses(cls):
    subclasses = []
    for subclass in cls.__subclasses__():
        subclasses.append(subclass)
        subclasses.extend(get_all_subclasses(subclass))
    return subclasses

class Library:
    def __init__(self, name):
        self.name = name
        self.items = {}
        self.transactions = []
        self.librarians = []

    def add_librarian(self, name, email, admin_id):
        librarian = Librarian(name, email, admin_id, self)
        self.librarians.append(librarian)
        return librarian
    def add_librarian(self, librarian):
        librarian = Librarian(librarian.name, librarian.email, librarian.admin_id, self)
        self.librarians.append(librarian)
        return librarian

    def list_librarians(self):
        return [librarian for librarian in self.librarians]

    def add_item(self, item):
        if item.isbn in self.items:
            self.items[item.isbn].add_copy()
        else:
            self.items[item.isbn] = item
        self.record_transaction("added", item, self.librarians[0] if self.librarians else None)

    def remove_item(self, isbn):
        if isbn in self.items:
            item = self.items[isbn]
            self.record_transaction("removed", item, self.librarians[0] if self.librarians else None)
            del self.items[isbn]
        else:
            print("ISBN not found")
    def update_item(self, isbn):
        if isbn in self.items:
            item = self.items[isbn]
            item_type = item.get_type()
            subclasses = get_all_subclasses(LibraryItem)
            selected_class = next((sub for sub in subclasses if item_type == sub.get_type()), None)
            attrs = [a for a in selected_class.__init__.__code__.co_varnames if a != 'self']
            print("====== Update Menu ======")
            print("1. Update\n2. Exit")
            while True:
                try:
                    opt = int(input("Enter option: "))
                except ValueError:
                    print("Invalid option. Please enter a number.")
                    continue

                if opt == 2:
                    break
                elif opt != 1:
                    print("Invalid choice. Enter 1 or 2.")
                    continue
                for i, atr in enumerate(attrs, 1):
                    print(f"{i}. {atr}")
                try:
                    attr_to_update = int(input("Choose field to update: ")) - 1
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
                if not (0 <= attr_to_update < len(attrs)):
                    print("Invalid choice. Please select a valid attribute.")
                    continue
                attr_name = attrs[attr_to_update]
                if hasattr(item, attr_name):
                    raw_value = input(f"Enter new {attr_name}: ")
                    current_value = getattr(item, attr_name)
                    target_type = type(current_value)
                    try:
                        if target_type is bool:
                            value = raw_value.lower() in ("true", "1", "yes", "y")
                        else:
                            value = target_type(raw_value)
                    except Exception:
                        print(f"Invalid input: expected {target_type.__name__}. Try again.")
                        continue
                    if attr_name == "isbn":
                        old_isbn = item.isbn
                        setattr(item, attr_name, value)
                        self.items[value] = self.items.pop(old_isbn)
                        print(f"ISBN updated successfully from {old_isbn} to {value}")
                    else:
                        setattr(item, attr_name, value)
                        print(f"{attr_name} updated successfully to {value}")
                else:
                    print(f"Attribute '{attr_name}' not found in {item.get_type()}")
                print("1. Update\n2. Exit")


    def get_item(self,isbn):
        if isbn in self.items:
            return self.items[isbn]
    def list_items(self):
        if not self.items:
            print("No items in the library.")
            return []
        item_types = sorted(set(item.get_type() for item in self.items.values()))
        print("\nChoose which items to view:")
        index = 1
        for type in item_types:
            print(f"{index}. {type}")
            index += 1
        print(f"{index}. All Items")
        choice = input("Enter choice: ")

        filtered_items = []

        try:
            choice = int(choice)
            if 1 <= choice <= len(item_types):
                selected_type = item_types[choice - 1]
                filtered_items = [str(item) for item in self.items.values() if item.get_type() == selected_type]
            elif choice == len(item_types) + 1:
                filtered_items = [str(item) for item in self.items.values()]
            else:
                print("Invalid choice. Showing all items by default.")
                filtered_items = [str(item) for item in self.items.values()]
        except ValueError:
            print("Invalid input. Showing all items by default.")
            filtered_items = [str(item) for item in self.items.values()]

        return filtered_items



    def record_transaction(self, transaction_type, item, librarian=None):
        if librarian:
            t = Transaction(librarian, item, transaction_type)
            self.transactions.append(t)

    def list_transactions(self):
        return [str(t) for t in self.transactions]

    def __del__(self):
        print(f"Library '{self.name}' deleted. All librarians removed.")
        self.librarians.clear()