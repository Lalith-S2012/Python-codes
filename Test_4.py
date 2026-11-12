class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

def borrow(self):
    if not self.is_borrowed:
        self.is_borrowed = True
        print(f"Confirmation: You borrowed '{self.title}' by '{self.author}'")

    else: 
        print("Sorry, the book you chose has already been borrowed")

def return_book(self):
    if self.is_borrowed:
        self.is_borrowed = False
        print("Confirmation: You already returned the book")

    else:
        print("you did not borrow a book")

book1 = Book("Charlottes Web", "Lalith")
book2 = Book("Diary of a Wimpy Kid", "William")
book3 = Book("Goodnoght Mister Tom", "Reuben")

print("Testing Book1")
book1.borrow()
book1.return_book()

print("Testing Book2")
book2.borrow()
book2.return_book()

print("Testing Book3")
book3.borrow()
book3.return_book()