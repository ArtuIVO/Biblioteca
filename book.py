class Book:
    def __init__(self, isbn: int, title: str, author: str):
        self.isbn = isbn
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.isbn} - {self.title} - {self.author}"
