### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
'''def input_book_info():
    title = input("Enter the book's title: ")
    author = input("Enter the book's author: ")
    year = int(input("Enter the book's publication year: "))
    rating = float(input("Enter the book's rating: "))
    pages = int(input("Enter the number of pages in the book: "))

    return {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

user_book = input_book_info()
print("User's book information:")
print(user_book)'''

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

'''def input_book_info():
    title = input("Enter the book's title: ")
    author = input("Enter the book's author: ")
    year = int(input("Enter the book's publication year: "))
    rating = float(input("Enter the book's rating: "))
    pages = int(input("Enter the number of pages in the book: "))

    return {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

user_book = input_book_info()
print("User's book information:")
print(user_book)'''

### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here
'''def get_valid_year():
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
            pages = int(input("Enter the number of pages in the book: "))
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

            # If all inputs are successful, return the book details
            return {
                "title": title,
                "author": author,
                "year": year,
                "rating": rating,
                "pages": pages
            }

        except KeyboardInterrupt:
            print("\nInput interrupted. Please try again.")
        except Exception as e:
            print("An unexpected error occurred:", e)

user_book = input_book_info()
print("User's book information:")
print(user_book)'''
### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
library = []

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
            pages = int(input("Enter the number of pages in the book: "))
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

            # If all inputs are successful, return the book details
            return {
                "title": title,
                "author": author,
                "year": year,
                "rating": rating,
                "pages": pages
            }
        except KeyboardInterrupt:
            print("\nInput interrupted. Please try again.")
        except Exception as e:
            print("An unexpected error occurred:", e)
        menu()


def modifyBooks(book, prop, newValue):
    for books in library:
        for key, value in books.items():
            if value.lower() == book.lower() and prop in books:
                books[prop] = newValue
                return f"{prop} has been changed to '{newValue}'"
        return f"Unknown property or book: {book}"
    
class QuitException(Exception):
    pass

def modBookHandler():
    try: 

        title = input("Enter the title of your book you wish to modify:")

        if not any(book['title'].lower() == title.lower() for book in library):
            print(f"Book with title '{title}' not found in the library.")
            modBookHandler()
            return

        print('Enter the property you wish to change.')
        print('1. author')
        print('2. year')
        print('3. rating')
        print('4. pages')
        print('5. quit')

        choice = int(input("Enter your choice: "))

        if choice == 1:
            newValue = input("Enter the new author value: ")
        elif choice == 2:
            newValue = get_valid_year()
        elif choice == 3:
            newValue = get_valid_rating()
        elif choice == 4:
            newValue = get_valid_pages()
        elif choice == 5:
            print("Goodbye!")
            raise QuitException
        else:
            print("Please enter a valid choice (1, 2, 3, 4, or 5).")        


        modifyBooks(title, choice, newValue)
        menu()
    except ValueError:
        print("Invalid input. Please try again.")

def allBooks():
    for books in library:
        title, author, year, rating, pages = books.values()
        book_string = f'{title} was written by {author} in the year {year}. It has a {rating} star rating and is {pages} pages.'
        print(book_string)




def menu():
    while True:
            try:
                print("MENU:")
                print("1. Add a new book")
                print("2. See all books")
                print("3. Edit a book")
                print("4. Quit")

                choice = int(input("Enter your choice: "))
                
                if choice == 1:
                    library.append(input_book_info())
                    print("Book added to the library.")
                elif choice == 2:
                    if len(library) < 1:
                        print("No books in the library yet. Add a new book first!")
                    else: allBooks()
                elif choice == 3:
                    if len(library) < 1:
                        print("No books in the library yet. Add a new book first!")
                    else:
                        modBookHandler()
                elif choice == 4:
                    print("Goodbye!")
                    break
                else:
                    print("Please enter a valid choice (1, 2, 3, or 4).")

            except ValueError:
                print("Invalid input. Please enter a valid choice.")

menu()


### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

