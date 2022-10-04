class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayAvailableBooks(self):
        print("Books present in this library are :")
        for book in self.books:
            print(" * " + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it with in 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book has already been issued to someone else. Please wait until the book is returned.")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returing this book! Hope you enjoyed reading it. Have a great day ahead!")

class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow :")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return :")
        return self.book


if __name__ == "__main__":
    centraLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes"])
    student = Student()
    while(True):
        welcomeMsg = '''***** Welcome to Central Library *****\n
Please choose an option:
1. Listing all books
2. Request a book
3. Return a book
4. Exit the library\n'''

        print(welcomeMsg)

        a= int(input("Enter a chocie : "))
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centraLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library. Have a Great day ahead!")
            exit()
        else:
            print("Invalid Choice!")
