# Library Management System (Admin Only)

A simple **console-based Library Management System** built using **Object-Oriented Programming (OOP) principles in Python**.
It allows an administrator (librarian) to manage books, magazines, journals, and newspapers.

---

## Features

* **Add Items**

  * Add Book
  * Add Magazine
  * Add Journal
  * Add Newspaper

* **Manage Items**

  * Remove existing items
  * Update item details
  * Get details of a single item
  * View all available items

* **Transaction Logs**

  * Track all additions, deletions, and updates made in the system

* **Exit Option**

  * Cleanly terminate the program

---

## Class Structure

The project is built with modular **OOP principles**:

* **Person** → Base class
* **Librarian(Person)** → Manages the library
* **Item** → Base class for all library items

  * **Book(Item)**
  * **Magazine(Item)**
  * **Journal(Item)**
  * **Newspaper(Item)**
* **Library** → Holds collections of items and manages operations
* **Transaction** → Records and monitors all operations performed

---

## Menu Options

```text
===== Library Management (Admin Only) =====
1. Add Book
2. Add Magazine
3. Add Journal
4. Add Newspaper
5. Remove Item
6. Update Item
7. View All Items
8. View Transactions
9. Get Single Item
10. Exit
Enter choice (1-10):
```

---

## Installation & Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/library-management.git
   ```
2. Navigate to the project folder:

   ```bash
   cd library-management
   ```
3. Run the program:

   ```bash
   python arc/main.py
   ```

---

## 📖 Example Usage

* Adding a book:

  ```
  Enter choice (1-10): 1
  Enter Book Title: Python Basics
  Enter Author: John Doe
  Enter ISBN: 12345
  Book added successfully!
  ```

* Viewing transactions:

  ```
  Enter choice (1-10): 8
  Transactions:
  [2025-08-20] Added Book: Python Basics
  ```

---

## Future Improvements

* Add user roles (Member, Guest)
* Implement borrowing/returning system
* Store data in a database (SQLite/MySQL)
* Add GUI or web interface

---

##  Author

**Inamullah Shaikh**

---
