class Library:
    def __init__(self,libName):
        self.libName = libName
        self.books = []

    def addBook(self,book):
        self.books.append(book)
        
    def showBook(self):
        return [f"{book.bookName} by {book.author}" for book in self.books]

class Book:
    def __init__(self,bookName,author):
        self.bookName = bookName
        self.author = author

#the lib1 and book1,2,3 objects are independent of each others and can function on their own 
#but the lib1 hold the book1,2,3 this thing is called aggregation
lib1 = Library("New York Library")

book1 = Book("Physics","HC Verma")
book2 = Book("Harry Potter","J.K. Rowling")
book3 = Book("Maths","RD Sharma")

lib1.addBook(book1)
lib1.addBook(book2)
lib1.addBook(book3)

print(lib1.libName)
for book in lib1.showBook():
    print(book)