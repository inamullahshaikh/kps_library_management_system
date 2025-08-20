from core.library import Library
from people.librarian import Librarian
from items.book import Book
from items.magazine import Magazine
from items.journal import Journal
from items.newspaper import Newspaper

def get_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}. Try again.")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must not exceed {max_val}. Try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_nonempty_string(prompt):
    while True:
        value = input(prompt).strip()
        if not value:
            print("This field cannot be empty. Try again.")
        else:
            return value

def get_isbn(prompt, library=None):
    while True:
        isbn = input(prompt).strip()
        if not isbn:
            print("ISBN cannot be empty.")
            continue
        if library and isbn in library.items:
            print("This ISBN already exists in the library. Enter a different one.")
            continue
        return isbn

def main():
    library = Library("City Library")
    librarian = Librarian("Alice", "alice@lib.com", "A001", library)
    library.add_librarian(librarian)

    while True:
        print("\n===== Library Management (Admin Only) =====")
        print("1. Add Book")
        print("2. Add Magazine")
        print("3. Add Journal")
        print("4. Add Newspaper")
        print("5. Remove Item")
        print("6. Update Item")
        print("7. View All Items")
        print("8. View Transactions")
        print("9. Get Single Item")
        print("10. Exit")

        choice = input("Enter choice (1-10): ").strip()

        if choice == "1":  
            title = get_nonempty_string("Enter book title: ")
            author = get_nonempty_string("Enter author: ")
            isbn = get_isbn("Enter ISBN: ", library)
            copies = get_int("Enter number of copies: ", min_val=1)
            genre = get_nonempty_string("Enter genre: ")
            book = Book(title, author, isbn, copies, genre)
            librarian.add_item(book)

        elif choice == "2":
            title = get_nonempty_string("Enter magazine title: ")
            author = get_nonempty_string("Enter author: ")
            isbn = get_isbn("Enter ISBN: ", library)
            copies = get_int("Enter number of copies: ", min_val=1)
            issue = get_nonempty_string("Enter issue number: ")
            mag = Magazine(title, author, isbn, copies, issue)
            librarian.add_item(mag)

        elif choice == "3":  
            title = get_nonempty_string("Enter journal title: ")
            author = get_nonempty_string("Enter researcher/author: ")
            isbn = get_isbn("Enter ISBN: ", library)
            copies = get_int("Enter number of copies: ", min_val=1)
            volume = get_nonempty_string("Enter volume: ")
            journal = Journal(title, author, isbn, copies, volume)
            librarian.add_item(journal)

        elif choice == "4": 
            title = get_nonempty_string("Enter newspaper title: ")
            author = get_nonempty_string("Enter author: ")
            isbn = get_isbn("Enter ISBN: ", library)
            copies = get_int("Enter number of copies: ", min_val=1)
            date = get_nonempty_string("Enter date (YYYY-MM-DD): ")
            newspaper = Newspaper(title, author, isbn, copies, date)
            librarian.add_item(newspaper)

        elif choice == "5":  
            isbn = get_nonempty_string("Enter ISBN to remove: ")
            librarian.remove_item(isbn)

        elif choice == "6":  
            isbn = get_nonempty_string("Enter ISBN to update: ")
            if isbn not in library.items:
                print("Item not found.")
            else:
                librarian.update_item(isbn)

        elif choice == "7": 
            print("\nItems in library:")
            for item in library.list_items():
                print(item)

        elif choice == "8":  
            print("\nTransactions:")
            for t in library.list_transactions():
                print(t)

        elif choice == "9":  
            isbn = get_nonempty_string("Enter ISBN: ")
            librarian.view_item(isbn)            

        elif choice == "10":
            print("Exiting...")
            break

        else:
            print("Invalid choice, please enter a number from 1 to 9.")
if __name__ == "__main__":
    main()
