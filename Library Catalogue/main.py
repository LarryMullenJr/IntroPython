class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def checkout(self):
        if self.available:
            self.available = False
            print(f"The book '{self.title}' by {self.author} has been checked out.")
        else:
            print(f"The book '{self.title}' by {self.author} is not available.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"The book '{self.title}' by {self.author} has been returned.")
        else:
            print(f"The book '{self.title}' by {self.author} is already available.")

class LibraryCatalogue:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Added '{title}' by {author} to the catalogue.")

    def display_catalogue(self):
        print("Library Catalogue:")
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Available: {book.available}")

def main():
    # Create a LibraryCatalogue instance
    catalogue = LibraryCatalogue()

    # Add books to the catalogue
    catalogue.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    catalogue.add_book("To Kill a Mockingbird", "Harper Lee")
    catalogue.add_book("1984", "George Orwell")

    # Display the catalogue
    catalogue.display_catalogue()

    # Checkout a book
    catalogue.books[0].checkout()

    # Return a book
    catalogue.books[0].return_book()

    # Display the catalogue after interactions
    catalogue.display_catalogue()

if __name__ == "__main__":
    main()