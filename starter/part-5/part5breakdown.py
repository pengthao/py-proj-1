class Book:
    def __init__(self, index, title, author, year, rating, pages):
        self.index = index
        self.title = title
        self.author = author
        self.year = year
        self.rating = rating
        self.pages = pages
        self.deleted = False

    def display_details(self):
        return f"{self.title} by {self.author} ({self.year}) - {self.rating} stars, {self.pages} pages."
    
    def mark_as_deleted(self):
        self.deleted = True

    def to_dictionary(self):
        return {
            "index": self.index,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "rating": self.rating,
            "pages": self.pages,
            "deleted": self.deleted
        }

'''
This segment of my code is to create a class using lines from the text file. Init is the function to instantiate the object.
display details is a fucntion that calls to properties of the object and returns information based on those properties
mark as deleted function is to set the deleted property so that when we write to the list again it knows which items to ignore
to dictionary function converts text file lines to an object

'''

def read_library():
    library = []
    with open("library.txt", "r") as fRead:
        for line in fRead:
            values = line.strip().split(", ")
            if len(values) == 6:
                index, title, author, year, rating, pages = values
                # turns lines from txt to book objects
                book_instance = Book(
                    index=int(index),
                    title=title,
                    author=author,
                    year=int(year),
                    rating=float(rating),
                    pages=int(pages)
                )
                library.append(book_instance)
            else:
                print(f"Skipping invalid line: {line}")

    return library


'''
read library opens the text file and splits the line by stripping away any extra spacing and splitting by ","
If all 6 properties are there i proceed with creating my Book object. i have destructured my variables to apply in the initialization.
append that new book object to the library list.
otherwise, skip the line
return library
    
'''
#This has been updated
def write_to_library_file(library, file_path="library.txt"):
    main_library = read_library()

    # Update existing books and mark deleted books
    for book in library:

        # Check if the book with the same index exists in main_library
        existing_books = [existing_book for existing_book in main_library if existing_book.index == book.index]

        if existing_books:
            # Update the existing book with the new information
            existing_book = existing_books[0]
            existing_book.title = str(book.title)
            existing_book.author = str(book.author)
            existing_book.year = int(book.year)
            existing_book.rating = float(book.rating)
            existing_book.pages = int(book.pages)
            existing_book.deleted = book.deleted  # Update deleted flag
        else:
            # If the book with the same index doesn't exist, add the new book to main_library
            main_library.append(book)

    # Exclude deleted books when writing to the file
    with open(file_path, "w") as file:
        for book in main_library:
            if not getattr(book, 'deleted', False):
                file.write(f"{book.index}, {book.title}, {book.author}, {book.year}, {book.rating}, {book.pages}\n")

'''
write library to file function will provide a list of book objects as an argument
i re-call my read_library function as main_library to have the main reference point.
for each book in my argument library, if the index number of my main library matches the argument library update the main library with the argument library's version
of the book's properties. If it isnt on my main library then add it to the main library.

When the function writes to the text file, it looks through my books in the main library. If the book does attribute deleted is not true then write the book object to the text file.
if getattr(book, 'deleted') this would say if the book value deleted is true. ifnot inverts we dont want to write books that have been deleted.

I had a lot of type issues which is why i had so much extra stuff padded in the to_dictionary. The code seems to be functioning with this simplified version now. Thank you!


'''

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

"""
These 3 functions are used to validate inputs so any inputs will return an error propmt until the correct data is entered

while true try return (int, float, in range)(input('some query for user')) 


"""

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


"""

the generate filter is used in my search_books() function. Theres a menu to select by ratings, pages, publishing year.
which when selected will call the validator functions and return that value

--snippet from search_books()-- 

print("2. Search by ratings")
    elif choice == 2:
        display_all_books(findGoodBooks(get_valid_rating()))

So the findgoodbooks function calls generate filters function passing in 'rating', and an annonymous function giving a comparison when given x and y. x is greater than y
We are also passing in the valid ratings. Say we entered 3.4

filter_books passes 3.4 as the argument
for each book in my library if the function comparison x>y for (the attribute passed 'rating' for current book), is greater than the value(3.4)
append the book

return the book list.

"""