class Book:
    def __init__(self, title: str, author: str, year: int):
        """Initialize a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Print a message when the book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self) -> str:
        """Return a user-friendly string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """Return an official string representation that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"