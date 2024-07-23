class Book:
    def __init__(self, title, author, genre, publication_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.borrower = None

    def __str__(self):
        return (f"{self.title} by {self.author} ({self.genre}, {self.publication_date})"
                f" - Borrowed by: {self.borrower.name if self.borrower else 'Available'}")
