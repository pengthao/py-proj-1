my_book = [{
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
},
{
    "title": "1984",
    "author": "George Orwell",
    "year": 1949,
    "rating": 4.89,
    "pages": 328
},
{
    "title": "Twilight",
    "author": "Stephenie Meyer",
    "year": 2005,
    "rating": 3.65,
    "pages": 498
},
]

# Follow the instructions in this part of the project. 
#Define and flesh out your function below, which should accept a dictionary as an argument when called, 
#and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below


def books_overview():
    book_summary = []
    for books in my_book:
        title, author, year, rating, pages = books.values()
        book_string = f'{title} was written by {author} in the year {year}. It has a {rating} star rating and is {pages} pages.'
        book_summary.append(book_string)
    return book_summary

print(books_overview())
# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

def search_book(query):
    found = False
    
    for book in my_book:
        if query.lower() in book['title'].lower() or query.lower() in book['author'].lower():
            found = True
            title, author, year, rating, pages = book['title'], book['author'], book['year'], book['rating'], book['pages']
            print(f'{title} was written by {author} in the year {year}. It has a {rating} star rating and is {pages} pages.')
    
    if not found:
        print('Your book was not found.')

search_book("The Hunger Games")

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def findBookProperty(book, prop):
    for books in my_book:
        for key, value in books.items():
            if value.lower() == book.lower() and prop in books:
                return books[prop]
        return f"Unknown property or book: {book}"

test = findBookProperty("The Hunger Games", "rating")
print(test)

def findGoodBooks(rating):
    book_list = []
    for books in my_book:
        if books['rating'] > rating:
            book_list.append(books['title'])
    
    return book_list

print(findGoodBooks(4.0))

def shortBooks(pages):
    book_list = []
    for books in my_book:
        if books['pages'] < pages:
            book_list.append(books['title'])
    
    return book_list

print(shortBooks(350))

def newerBooks(year):
    book_list = []
    for books in my_book:
        if books['year'] > year:
            book_list.append(books['title'])
    
    return book_list

print(newerBooks(2000))


#I was copying an pasting functions so i thought I could ask chatgpt for help with writing a factory function to replace the ones I have.
def generate_filter_function(attribute, comparison):
    def filter_books(value):
        book_list = []
        for book in my_book:
            if comparison(book[attribute], value):
                book_list.append(book['title'])
        return book_list
    return filter_books

findGoodBooks = generate_filter_function('rating', lambda x, y: x > y)
shortBooks = generate_filter_function('pages', lambda x, y: x < y)
newerBooks = generate_filter_function('year', lambda x, y: x > y)

# Test the generated functions
print(findGoodBooks(4.0))
print(shortBooks(350))
print(newerBooks(2000))


def generate_sort_function(attribute):
    def sort_books():
        return sorted(my_book, key=lambda x: x[attribute])
    return sort_books

sort_by_title = generate_sort_function('title')()
sort_by_author = generate_sort_function('author')()
sort_by_rating = generate_sort_function('rating')()
sort_by_pages = generate_sort_function('pages')()

def print_books(books):
    for book in books:
        print(book)

print("Sorted by title:")
print_books(sort_by_title)

print("\nSorted by author:")
print_books(sort_by_author)

print("\nSorted by rating:")
print_books(sort_by_rating)

print("\nSorted by pages:")
print_books(sort_by_pages)