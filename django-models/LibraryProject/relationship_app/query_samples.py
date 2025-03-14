from relationship_app.models import Book, Author, Library, Librarian

#query all books from a specific author
def get_book_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

#list all books in library
def list_books_in_library(library):
   library =  Library.objects.get(name=library)
   return library.books.all()
    

#retrieve the library of a librarian
def get_library_of_librarian(librarian):
    librarian = Librarian.objects.get(name=librarian)
    return librarian.library