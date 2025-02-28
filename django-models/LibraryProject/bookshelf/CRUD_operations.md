#import Book model from app
from bookshelf import Book

#create a book instance
book = Book.objects.create(title= "1984", author= "George Orwell", publication_year= 1949)
print(book)

Output:
    Book object(1)
    

#retrieve book
print (book.title, book.author, book.publication_year)

Output:
1984 George Orwell 1949

#Update the title of “1984” to “Nineteen Eighty-Four”
book.title = "Nineteen Eighty-Four"
print(book.title)

Output:
Nineteen Eighty-Four

#delete book
del book
print(book)

Output:
NameError: name 'book' is not defined.





