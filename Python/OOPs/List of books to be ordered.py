#List of books to be ordered
books = {
    "Harry Potter": 10,
    "Lord of the Rings": 5,
    "Game of Thrones": 2,
    "The Hunger Games": 8,
    "To Kill a Mockingbird": 4
}

def books_Order(bs):
    Required_books ={}
    Book_count = 10
    for name, qty in bs.items():
        Required_books[name] = Book_count - qty
    return Required_books

print(books_Order(books))