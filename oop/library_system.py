class Book:
    def __init__(self, title: str, author: str):
        """Initialize base Book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return string representation of Book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """Initialize EBook with additional file_size attribute."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return string representation of EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """Initialize PrintBook with additional page_count attribute."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return string representation of PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize Library with empty books list."""
        self.books = []

    def add_book(self, book: Book):
        """Add a book to the library collection."""
        self.books.append(book)

    def list_books(self):
        """Print details of all books in the library."""
        for book in self.books:
            print(book)