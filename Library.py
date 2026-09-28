# PROJECT 2 - LIBRARY MANAGEMENT SYSTEM


# ---------------- BOOK CLASS ----------------
class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True


# ---------------- MEMBER CLASS ----------------
class Member:

    def __init__(self, member_id, member_name):
        self.member_id = member_id
        self.member_name = member_name


# ---------------- LIBRARY SERVICE CLASS ----------------
class LibraryService:

    def __init__(self):
        self.books = []
        self.members = []


    # Add Book
    def add_book(self):

        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)

        self.books.append(book)

        print("Book Added Successfully")


    # Remove Book
    def remove_book(self):

        book_id = input("Enter Book ID to Remove: ")

        for book in self.books:

            if book.book_id == book_id:

                self.books.remove(book)

                print("Book Removed Successfully")
                return

        print("Book Not Found")


    # Add Member
    def add_member(self):

        member_id = input("Enter Member ID: ")
        member_name = input("Enter Member Name: ")

        member = Member(member_id, member_name)

        self.members.append(member)

        print("Member Added Successfully")


    # Search Book
    def search_book(self):

        book_id = input("Enter Book ID to Search: ")

        for book in self.books:

            if book.book_id == book_id:

                print("Book Found")
                print("Book ID:", book.book_id)
                print("Title:", book.title)
                print("Author:", book.author)

                if book.available:
                    print("Status: Available")
                else:
                    print("Status: Issued")

                return

        print("Book Not Found")


    # Issue Book
    def issue_book(self):
        book_id = input("Enter Book ID to Issue: ")

        for book in self.books:

            if book.book_id == book_id:

                if book.available:

                    book.available = False

                    print("Book Issued Successfully")

                else:

                    print("Book is Not Available")

                return

        print("Book Not Found")


    # Return Book
    def return_book(self):

        book_id = input("Enter Book ID to Return: ")

        for book in self.books:

            if book.book_id == book_id:

                book.available = True

                print("Book Returned Successfully")

                
            else:

                print("Book Not Found")


    # Display All Books
    def display_books(self):

        if len(self.books) == 0:

            print("No Books Available")
            return

        print("\n----- ALL BOOKS -----")

        for book in self.books:

            print("Book ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)

            if book.available:
                print("Status: Available")
            else:
                print("Status: Issued")

            print("--------------------")


    # Display Available Books
    def display_available_books(self):

        found = False

        print("\n----- AVAILABLE BOOKS -----")

        for book in self.books:

            if book.available:

                found = True

                print("Book ID:", book.book_id)
                print("Title:", book.title)
                print("Author:", book.author)

                print("--------------------")

        if not found:

            print("No Available Books")


# ---------------- MAIN PROGRAM ----------------

library = LibraryService()


while True:

    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")

    print("1. Add Book")
    print("2. Remove Book")
    print("3. Add Member")
    print("4. Search Book")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Display All Books")
    print("8. Display Available Books")
    print("9. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":

        library.add_book()


    elif choice == "2":

        library.remove_book()


    elif choice == "3":

        library.add_member()


    elif choice == "4":

        library.search_book()


    elif choice == "5":

        library.issue_book()


    elif choice == "6":

        library.return_book()


    elif choice == "7":

        library.display_books()


    elif choice == "8":

        library.display_available_books()


    elif choice == "9":

        print("Thank You!")
        break


    else:

        print("Invalid Choice")