from book import Book
from author import Author
from borrower import Borrower
from user import User
import datetime
class Library:
    def __init__(self):
        self.books = []
        self.authors = set()
        self.borrowers = set()
        self.users = {"admin": "admin"}

    def add_user(self, username, password):
        if username in self.users:
            return False
        self.users[username] = password
        return True

    def authenticate_user(self, username, password):
        return self.users.get(username) == password

    def add_book(self, book):
        author = next((a for a in self.authors if a.name.lower() == book.author.lower()), None)
        if not author:
            author = Author(book.author)
            self.add_author(author)
        author.books.append(book)
        self.books.append(book)

    def list_books(self):
        if not self.books:
            return "No books available!"
        return "\n".join(str(book) for book in self.books)

    def search_books(self, title=None, author=None, genre=None):
        results = self.books
        if title:
            results = [book for book in results if title.lower() in book.title.lower()]
        if author:
            results = [book for book in results if author.lower() in book.author.lower()]
        if genre:
            results = [book for book in results if genre.lower() in book.genre.lower()]
        return results

    def sort_books(self, key):
        return sorted(self.books, key=lambda book: getattr(book, key))

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title.lower() != title.lower()]

    def add_author(self, author):
        self.authors.add(author)

    def list_authors(self):
        if not self.authors:
            return "No authors available!"
        return "\n".join(str(author) for author in self.authors)

    def search_authors(self, name):
        return [author for author in self.authors if name.lower() in author.name.lower()]

    def sort_authors(self, key):
        return sorted(self.authors, key=lambda author: getattr(author, key))

    def remove_author(self, name):
        author = next((a for a in self.authors if a.name.lower() == name.lower()), None)
        if author:
            if any(book.borrower for book in author.books):
                return f"Author '{name}' can't be deleted because their books are borrowed."
            self.authors.remove(author)
            self.books = [book for book in self.books if book.author.lower() != name.lower()]
            return f"Author '{name}' and their books removed successfully."
        return f"Author '{name}' not found."

    def add_borrower(self, borrower):
        self.borrowers.add(borrower)

    def list_borrowers(self):
        if not self.borrowers:
            return "No borrowers available!"
        return "\n".join(str(borrower) for borrower in self.borrowers)

    def search_borrowers(self, name):
        return [borrower for borrower in self.borrowers if name.lower() in borrower.name.lower()]

    def sort_borrowers(self, key):
        return sorted(self.borrowers, key=lambda borrower: getattr(borrower, key))

    def remove_borrower(self, name):
        borrower = next((b for b in self.borrowers if b.name.lower() == name.lower()), None)
        if borrower:
            if borrower.borrowed_books:
                return f"Borrower '{name}' can't be deleted because they have borrowed books."
            self.borrowers.remove(borrower)
            return f"Borrower '{name}' removed successfully."
        return f"Borrower '{name}' not found."

    def borrow_book(self, book_title, borrower_name):
        book = next((book for book in self.books if book.title.lower() == book_title.lower()), None)
        borrower = next((borrower for borrower in self.borrowers if borrower.name.lower() == borrower_name.lower()), None)
        if not borrower:
            borrower = Borrower(borrower_name)
            self.add_borrower(borrower)
        if book and not book.borrower:
            book.borrower = borrower
            borrower.borrowed_books.append(book)
            return f"Book '{book_title}' borrowed by {borrower_name}"
        return "Book is not available or Borrower not found"

    def return_book(self, book_title):
        book = next((book for book in self.books if book.title.lower() == book_title.lower()), None)
        if book and book.borrower:
            book.borrower.borrowed_books.remove(book)
            book.borrower = None
            return f"Book '{book_title}' returned"
        return "Book not found or not borrowed"
