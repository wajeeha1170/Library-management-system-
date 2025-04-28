class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} (Available: {self.quantity})"

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author, quantity):
        if book_id in self.books:
            print("Book ID already exists. Updating quantity.")
            self.books[book_id].quantity += quantity
        else:
            self.books[book_id] = Book(book_id, title, author, quantity)
            print("Book added successfully.")

    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            for book in self.books.values():
                print(book)

    def borrow_book(self, book_id):
        if book_id in self.books and self.books[book_id].quantity > 0:
            self.books[book_id].quantity -= 1
            print(f"You have borrowed: {self.books[book_id].title}")
        else:
            print("Book not available.")

    def return_book(self, book_id):
        if book_id in self.books:
            self.books[book_id].quantity += 1
            print(f"Thank you for returning: {self.books[book_id].title}")
        else:
            print("Invalid book ID.")

def main():
    library = Library()

    while True:
        print("\n----- Library Management System -----")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            quantity = int(input("Enter Quantity: "))
            library.add_book(book_id, title, author, quantity)

        elif choice == '2':
            library.display_books()

        elif choice == '3':
            book_id = input("Enter Book ID to borrow: ")
            library.borrow_book(book_id)

        elif choice == '4':
            book_id = input("Enter Book ID to return: ")
            library.return_book(book_id)

        elif choice == '5':
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Please select between 1-5.")

if __name__ == "__main__":
    main()class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} (Available: {self.quantity})"

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author, quantity):
        if book_id in self.books:
            print("Book ID already exists. Updating quantity.")
            self.books[book_id].quantity += quantity
        else:
            self.books[book_id] = Book(book_id, title, author, quantity)
            print("Book added successfully.")

    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            for book in self.books.values():
                print(book)

    def borrow_book(self, book_id):
        if book_id in self.books and self.books[book_id].quantity > 0:
            self.books[book_id].quantity -= 1
            print(f"You have borrowed: {self.books[book_id].title}")
        else:
            print("Book not available.")

    def return_book(self, book_id):
        if book_id in self.books:
            self.books[book_id].quantity += 1
            print(f"Thank you for returning: {self.books[book_id].title}")
        else:
            print("Invalid book ID.")

def main():
    library = Library()

    while True:
        print("\n----- Library Management System -----")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            quantity = int(input("Enter Quantity: "))
            library.add_book(book_id, title, author, quantity)

        elif choice == '2':
            library.display_books()

        elif choice == '3':
            book_id = input("Enter Book ID to borrow: ")
            library.borrow_book(book_id)

        elif choice == '4':
            book_id = input("Enter Book ID to return: ")
            library.return_book(book_id)

        elif choice == '5':
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Please select between 1-5.")

if __name__ == "__main__":
    main()
