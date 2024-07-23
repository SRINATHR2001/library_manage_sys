from library import Library
from book import Book
from author import Author
from borrower import Borrower
from user import User
import datetime


def main():
    library = Library()
    logged_in_user = None

    while True:
        if not logged_in_user:
            print("\nLibrary Management System")
            print("1. Login")
            print("2. Signup")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                if library.authenticate_user(username, password):
                    logged_in_user = User(username, password)
                    logged_in_user.role = "admin" if username == "admin" else "user"
                    print(f"Welcome, {logged_in_user.username}!")
                else:
                    print("Invalid credentials. Please try again.")

            elif choice == "2":
                username = input("Enter username: ")
                password = input("Enter password: ")
                if library.add_user(username, password):
                    print("User registered successfully. Please login.")
                else:
                    print("Username already exists. Please try a different one.")

            elif choice == "3":
                break

            else:
                print("Invalid choice. Please try again.")

        else:
            print("\nLibrary Management System")
            print("1. Book Management")
            print("2. Author Management")
            print("3. Borrower Management")
            print("4. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                if logged_in_user.role == "admin":
                    print("\nBook Management")
                    print("1. Add Book")
                    print("2. List Books")
                    print("3. Search Books")
                    print("4. Sort Books")
                    print("5. Remove Book")
                    book_choice = input("Enter your choice: ")

                    if book_choice == "1":
                        title = input("Enter title: ")
                        author_name = input("Enter author: ")
                        genre = input("Enter genre: ")
                        publication_date = datetime.datetime.now().ctime()

                        book = Book(title, author_name, genre, publication_date)
                        library.add_book(book)
                        print("Book added successfully!")

                    elif book_choice == "2":
                        print(library.list_books())

                    elif book_choice == "3":
                        title = input("Enter title to search (leave blank if not applicable): ")
                        author = input("Enter author to search (leave blank if not applicable): ")
                        genre = input("Enter genre to search (leave blank if not applicable): ")
                        results = library.search_books(title, author, genre)
                        for book in results:
                            print(book)

                    elif book_choice == "4":
                        key = input("Enter sorting key (title, author, publication_date): ")
                        sorted_books = library.sort_books(key)
                        for book in sorted_books:
                            print(book)

                    elif book_choice == "5":
                        title = input("Enter title of the book to remove: ")
                        library.remove_book(title)
                        print(f"Book '{title}' removed successfully!")

                else:
                    print("\nBook Management")
                    print("1. List Books")
                    book_choice = input("Enter your choice: ")

                    if book_choice == "1":
                        print(library.list_books())

            elif choice == "2":
                if logged_in_user.role == "admin":
                    print("\nAuthor Management")
                    print("1. Add Author")
                    print("2. List Authors")
                    print("3. Search Authors")
                    print("4. Sort Authors")
                    print("5. Remove Author")
                    author_choice = input("Enter your choice: ")

                    if author_choice == "1":
                        name = input("Enter name: ")
                        author = Author(name)
                        library.add_author(author)
                        print("Author added successfully!")

                    elif author_choice == "2":
                        print(library.list_authors())

                    elif author_choice == "3":
                        name = input("Enter name to search: ")
                        results = library.search_authors(name)
                        for author in results:
                            print(author)

                    elif author_choice == "4":
                        key = input("Enter sorting key (name): ")
                        sorted_authors = library.sort_authors(key)
                        for author in sorted_authors:
                            print(author)

                    elif author_choice == "5":
                        name = input("Enter name of the author to remove: ")
                        print(library.remove_author(name))

                else:
                    print("\nAuthor Management")
                    print("1. List Authors")
                    author_choice = input("Enter your choice: ")

                    if author_choice == "1":
                        print(library.list_authors())

            elif choice == "3":
                print("\nBorrower Management")
                if logged_in_user.role == "admin":
                    print("1. Add Borrower")
                    print("2. List Borrowers")
                    print("3. Search Borrowers")
                    print("4. Sort Borrowers")
                    print("5. Remove Borrower")
                    print("6. Borrow Book")
                    print("7. Return Book")
                    borrower_choice = input("Enter your choice: ")

                    if borrower_choice == "1":
                        name = input("Enter name: ")
                        borrower = Borrower(name)
                        library.add_borrower(borrower)
                        print("Borrower added successfully!")

                    elif borrower_choice == "2":
                        print(library.list_borrowers())

                    elif borrower_choice == "3":
                        name = input("Enter name to search: ")
                        results = library.search_borrowers(name)
                        for borrower in results:
                            print(borrower)

                    elif borrower_choice == "4":
                        key = input("Enter sorting key (name): ")
                        sorted_borrowers = library.sort_borrowers(key)
                        for borrower in sorted_borrowers:
                            print(borrower)

                    elif borrower_choice == "5":
                        name = input("Enter name of the borrower to remove: ")
                        print(library.remove_borrower(name))

                    elif borrower_choice == "6":
                        book_title = input("Enter title of the book to borrow: ")
                        borrower_name = input("Enter name of the borrower: ")
                        print(library.borrow_book(book_title, borrower_name))

                    elif borrower_choice == "7":
                        book_title = input("Enter title of the book to return: ")
                        print(library.return_book(book_title))

                else:
                    print("1. List Borrowers")
                    print("2. Borrow Book")
                    print("3. Return Book")
                    borrower_choice = input("Enter your choice: ")

                    if borrower_choice == "1":
                        print(library.list_borrowers())

                    elif borrower_choice == "2":
                        book_title = input("Enter title of the book to borrow: ")
                        borrower_name = logged_in_user.username
                        print(library.borrow_book(book_title, borrower_name))

                    elif borrower_choice == "3":
                        book_title = input("Enter title of the book to return: ")
                        print(library.return_book(book_title))

            elif choice == "4":
                logged_in_user = None

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
