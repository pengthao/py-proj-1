from pprint import pprint
### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here


### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

class QuitException(Exception):
    pass

class Book:
    def __init__(self, index, title, author, year, rating, pages):
        self.index = index
        self.title = title
        self.author = author
        self.year = year
        self.rating = rating
        self.pages = pages
        self.deleted = False  # Initialize deleted flag to False

    def mark_as_deleted(self):
        self.deleted = True

    def to_dictionary(self):
        # Return a dictionary representation of the book
        return {
            'index': self.index,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'rating': self.rating,
            'pages': self.pages,
            'deleted': self.deleted  # Include deleted flag in the dictionary
        }
    
def read_library():
    library = []
    with open("library.txt", "r") as fRead:
        for line in fRead:
            title, author, year, rating, pages = line.strip().split(", ")

            book_dictionary = {
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            }

            library.append(book_dictionary)
    return library

def write_library_to_file(library, file_path="library.txt"):
    with open(file_path, "w") as file:
        for book in library:
            file.write(f"{book['title']}, {book['author']}, {book['year']}, {book['rating']}, {book['pages']}\n")

def write_to_library(book_info):
    with open("library.txt", "a") as fAppend:
        fAppend.write(f"{book_info['title']}, {book_info['author']}, {book_info['year']}, {book_info['rating']}, {book_info['pages']}\n")

def get_valid_year():
    while True:
        try:
            return int(input("Enter the book's publication year: "))
        except ValueError:
            print("Please enter a valid integer for the year.")

def get_valid_rating():
    while True:
        try:
            rating = float(input("Enter the book's rating: "))
            if 0.0 <= rating <= 5.0:
                return rating
            else:
                print("Please enter a rating between 0.0 and 5.0.")
        except ValueError:
            print("Please enter a valid number for the rating.")

def get_valid_pages():
    while True:
        try:
            pages = int(input("Enter the page number: "))
            if pages > 0:
                return pages
            else:
                print("Please enter a positive number of pages.")
        except ValueError:
            print("Please enter a valid integer for the pages.")

def input_book_info():
    while True:
        try:
            title = input("Enter the book's title: ")
            author = input("Enter the book's author: ")
            year = get_valid_year()
            rating = get_valid_rating()
            pages = get_valid_pages()

            book_info = {
                "title": title,
                "author": author,
                "year": year,
                "rating": rating,
                "pages": pages
            }

            write_to_library(book_info)
            library.append(book_info)
            return book_info
        
        except KeyboardInterrupt:
            print("\nInput interrupted. Please try again.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def modify_books(library, book_title, prop, new_value, file_path="library.txt"):
    for book in library:
        if book['title'].lower() == book_title.lower() and prop in book:
            book[prop] = new_value
            write_library_to_file(library, file_path) 
            return f"{prop} has been changed to '{new_value}'"
    return f"Unknown property or book: {book_title}"



def mod_book_handler(library):
    try: 
        title = input("Enter the title of your book you wish to modify:")

        if not any(book['title'].lower() == title.lower() for book in library):
            print(f"Book with title '{title}' not found in the library.")
            return

        print('Enter the property you wish to change.')
        print('1. author')
        print('2. year')
        print('3. rating')
        print('4. pages')
        print('5. quit')

        choice = int(input("Enter your choice: "))

        if choice == 1:
            new_value = input("Enter the new author value: ")
        elif choice == 2:
            new_value = get_valid_year()
        elif choice == 3:
            new_value = get_valid_rating()
        elif choice == 4:
            new_value = get_valid_pages()
        elif choice == 5:
            print("Goodbye!")
            raise QuitException
        else:
            print("Please enter a valid choice (1, 2, 3, 4, or 5).")        

        print(modify_books(library, title, choice, new_value))
    except ValueError:
        print("Invalid input. Please try again.")

def edit_book(library):
    try:
        book_number = int(input("Enter the number of the book you want to edit: "))
        book_index = book_number - 1
        if 0 <= book_index < len(library):
            book = library[book_index]
            title = book["title"]

            print('Enter the property you wish to change.')
            print('1. title')
            print('2. author')
            print('3. year')
            print('4. rating')
            print('5. pages')
            print('6. quit')

            choice = int(input("Enter your choice: "))

            if choice == 1:
                new_value = input("Enter the new title: ")
            elif choice == 2:
                new_value = input("Enter the new author: ")
            elif choice == 3:
                new_value = get_valid_year()
            elif choice == 4:
                new_value = get_valid_rating()
            elif choice == 5:
                new_value = get_valid_pages()      
            elif choice == 6:
                print("Goodbye!")
                raise QuitException  
            else:
                print("Please enter a valid choice (1, 2, 3, 4, 5, or 6).")             

            print(modify_books(library, title, choice, new_value))
        else:
            print("Invalid book number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def all_books(library):
    books_per_page = 10
    total_books = len(library)
    current_page = 1

    while True:
        start_index = (current_page - 1) * books_per_page
        end_index = start_index + books_per_page

        current_books = library[start_index:end_index]

        if not current_books:
            print("No more books to display.")
            break

        print(f"Page {current_page} of {total_books // books_per_page + 1}:")

        for i, book in enumerate(current_books, start=start_index + 1):
            title, author, year, rating, pages = book.values()
            book_string = f"{i}. {title} by {author} ({year}) - {rating} stars, {pages} pages."
            print(book_string)

        print("\n1. Next Page")
        print("2. Previous Page")
        print("3. Edit a Book")
        print("4. Return to Menu")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                current_page += 1
            elif choice == 2:
                if current_page > 1:
                    current_page -= 1
                else:
                    print("Already at the first page.")
            elif choice == 3:
                edit_book(library)
            elif choice == 4:
                print("Returning to Menu.")
                break 
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        

def menu(library):
    while True:
        try:
            print("MENU:")
            print("1. Add a new book")
            print("2. See all books")
            print("3. Edit a book")
            print("4. Quit")

            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                input_book_info()
                print("Book added to the library.")
            elif choice == 2:
                if not library:
                    print("No books in the library yet. Add a new book first!")
                else:
                    all_books(library)
            elif choice == 3:
                if not library:
                    print("No books in the library yet. Add a new book first!")
                else:
                    mod_book_handler(library)
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Please enter a valid choice (1, 2, 3, or 4).")

        except ValueError:
            print("Invalid input. Please enter a valid choice.")

if __name__ == "__main__":
    library = read_library()
    menu(library)