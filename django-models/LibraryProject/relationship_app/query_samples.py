from relationship_app.models import Book, Author, Library, Librarian

#query all books from a specific author
def get_book_by_author(Book):
    author = Author.object.get(name = author_name)
    return Book.objects.filter(author = author)

#list all books in library
def list_books_in_library(Library):
    return Library.objects.get(name=library_name)
    

#retrieve the library of a librarian
def get_library_of_librarian(Librarian):
    librarian = Librarian.objects.get(name = librarian_name)
    return librarian.library