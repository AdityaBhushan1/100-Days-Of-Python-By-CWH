class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []
    
    def addBook(self,book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def showInfo(self):
        print(f"The Library Contains: {self.no_of_books} Books")

l1 = Library()
l1.addBook("Harry Potter 1")
l1.addBook("Harry Potter 2")
l1.addBook("Harry Potter 3")
l1.showInfo()