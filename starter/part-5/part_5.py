
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

from pprint import pprint

'''
 - General Questions -
 What are the best practices for preparing prototypes for review? Lots of comments?
 When developing applications, do we typically code logic around user interface? Buttons for example or is that a seperate step?
 Make small


'''


class QuitException(Exception):
    pass
#initialize a book class
class Book:
    def __init__(self, title, author, year, rating, pages):
        self.title = title
        self.author = author
        self.year = year
        self.rating = rating
        self.pages = pages
#methods for the class
    def display_details(self):
        return f"{self.title} by {self.author} ({self.year}) - {self.rating} stars, {self.pages} pages."

    def to_dictionary(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "rating": self.rating,
            "pages": self.pages
        }
    
#text management
def read_library():
    library = []
    with open("library.txt", "r") as fRead:
        for line in fRead:
            title, author, year, rating, pages = line.strip().split(", ")
            #turns lines from txt to book objects
            book_instance = Book(
                title = title,
                author = author,
                year = int(year),
                rating = float(rating),
                pages = int(pages)

            )

            library.append(book_instance)
    return library

'''I am having issues with writing to file. Specifically, when I go through my search functions
I end up generating a new shorter list. If i make changes to that list and write them to the file
my lists gets shorter. If I append, then I end up with of the same books because they end up being different
books.

What is best practice when it comes to managing external data sources? 

'''

def write_to_library_file(library, file_path="library.txt"):
    main_library = read_library()

    with open(file_path, "w") as file:
        for existing_book in main_library:
            if existing_book not in library:
                file.write(f"{existing_book.to_dictionary()['title']}, {existing_book.to_dictionary()['author']}, {existing_book.to_dictionary()['year']}, {existing_book.to_dictionary()['rating']}, {existing_book.to_dictionary()['pages']}\n")

        for book in library:
            file.write(f"{book.to_dictionary()['title']}, {book.to_dictionary()['author']}, {book.to_dictionary()['year']}, {book.to_dictionary()['rating']}, {book.to_dictionary()['pages']}\n")

#validation
            
'''What are best practices surrounding very similar functions?'''

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

#search functions
            
def search_books(query, library):     
        book_list = []
        for book in library:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                book_list.append(book)
        return book_list

def generate_filter_function(attribute, comparison):
    def filter_books(value):
        book_list = []
        for book in library:
            if comparison(getattr(book, attribute), value):
                book_list.append(book)
        return book_list
    return filter_books

findGoodBooks = generate_filter_function('rating', lambda x, y: x > y)
shortBooks = generate_filter_function('pages', lambda x, y: x < y)
newerBooks = generate_filter_function('year', lambda x, y: x > y)


#add book

def add_book():
    while True:
        try:
            title = input("Enter the book's title: ")
            author = input("Enter the book's author: ")
            year = get_valid_year()
            rating = get_valid_rating()
            pages = get_valid_pages()

            book_info = Book(title, author, year, rating, pages)

            library.append(book_info)
            print(f"{book_info.title} added to the library.")

            write_to_library_file(library)

            break
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

#modify books

def delete_book(library, book):
    library.remove(book)

    write_to_library_file(library)
    print(f"{book.title} deleted from the library.")

def edit_book(library):
    try:
        book_number = int(input("Enter the number of the book you want to edit: "))
        book_index = book_number - 1
        if 0 <= book_index < len(library):
            book = library[book_index]

            print(f'Enter the action you wish to perform for {book.title}.')
            print('1. Edit')
            print('2. Delete')
            print('3. Quit')

            action_choice = int(input("Enter your choice: "))

            if action_choice == 1:
                print(f'Enter the property you wish to change for {book.title}.')
                print('1. title')
                print('2. author')
                print('3. year')
                print('4. rating')
                print('5. pages')
                print('6. quit')

                choice = int(input("Enter your choice: "))

                if choice == 1:
                    book.title = input("Enter the new title: ")
                elif choice == 2:
                    book.author = input("Enter the new author: ")
                elif choice == 3:
                    book.year = get_valid_year()
                elif choice == 4:
                    book.rating = get_valid_rating()
                elif choice == 5:
                    book.pages = get_valid_pages()      
                elif choice == 6:
                    print("Goodbye!")
                    raise QuitException  
                else:
                    print("Please enter a valid choice (1, 2, 3, 4, 5, or 6).")
                write_to_library_file(library)
            elif action_choice == 2:
                confirm_delete = input(f"Are you sure you want to delete {book.title}? (y/n): ").lower()
                if confirm_delete == 'y':
                    delete_book(library, book)
            elif action_choice == 3:
                print("Returning to menu.")
                quit
        else:
            print("Invalid book number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

#view books

def display_all_books(library):
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
            print(f"{i}. {book.display_details()}")

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

def search_books():
    while True:
        try:
            print("1. Search by title, or author")
            print("2. Search by ratings")
            print("3. Search by pages")
            print("4. Search by publishing year")
            print("5. Quit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                query = input("Enter title or author name: ").lower()
                display_all_books(search_books(query, library))
            elif choice == 2:
                display_all_books(findGoodBooks(get_valid_rating()))
            elif choice == 3:
                display_all_books(shortBooks(get_valid_pages()))
            elif choice == 4:
                display_all_books(newerBooks(get_valid_year()))
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                print("Please enter a valid choice (1, 2, 3, 4, 5, or 6).")

        except ValueError:
            print("Invalid input. Please enter a valid choice.")

#Menu 

def menu(library):
    while True:
        try:
            print("~ MAIN MENU ~")
            print("1. Add a new book")
            print("2. See all books")
            print("3. Search for a book")
            print("4. Quit")

            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                add_book()
                print("Book added to the library.")
            elif choice == 2:
                if not library:
                    print("No books in the library yet. Add a new book first!")
                else:
                    display_all_books(library)
            elif choice == 3:
                if not library:
                    print("No books in the library yet. Add a new book first!")
                else:
                    search_books()
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