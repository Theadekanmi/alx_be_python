class Book:
    """A class representing a book in a library management system."""
    
    def __init__(self, title, author):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability
    
    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Mark the book as returned if it was checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out
    
    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """A class representing a library that manages a collection of books."""
    
    def __init__(self):
        """Initialize a Library instance with an empty book collection."""
        self._books = []  # Private list to store books
    
    def add_book(self, book):
        """
        Add a book to the library's collection.
        
        Args:
            book (Book): The Book instance to add
        """
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise ValueError("Can only add Book objects to the library")
    
    def check_out_book(self, title):
        """
        Check out a book by title if available.
        
        Args:
            title (str): The title of the book to check out
        
        Returns:
            bool: True if successful, False if book not found or already checked out
        """
        for book in self._books:
            if book.title.lower() == title.lower() and book.is_available():
                return book.check_out()
        return False
    
    def return_book(self, title):
        """
        Return a checked out book by title.
        
        Args:
            title (str): The title of the book to return
        
        Returns:
            bool: True if successful, False if book not found or not checked out
        """
        for book in self._books:
            if book.title.lower() == title.lower() and not book.is_available():
                return book.return_book()
        return False
    
    def list_available_books(self):
        """Print all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No available books in the library")
        else:
            for book in available_books:
                print(book)