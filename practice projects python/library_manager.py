class library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def print_all_books(self):
        if self.no_of_books == 0:
            print("library is empty.")
        else:
            print("Books in the library: ")
            for book in self.books:
                print(book)

    def add_back(self, book_title):
        self.books.append(book_title)
        self.no_of_books += 1

    def get_number_of_books(self):
        return self.no_of_books


my_library = library()


while True:
    print("\n Library Menu: ")
    print("1. print all books")
    print("2. Add a book")
    print("3. get number of total books")
    print("3. Quit")

    choice = input("Enter your choice: (1/2/3/4) : ")

    if choice == "1":
        my_library.print_all_books()

    elif choice == "2":
        adding = input("Enter title of the book You want to add: ")
        my_library.add_back(adding)

    elif choice == "3":
        total_books = my_library.get_number_of_books()
        print(f"Total number of books in your library are : {total_books}")

    elif choice == "4":
        print("Quitting your library program.....")
        break

    else:
        print("Invalid choice ! please enter a valid option")
