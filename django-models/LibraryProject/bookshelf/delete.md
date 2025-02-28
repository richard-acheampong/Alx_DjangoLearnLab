#delete title book instance
from bookshelf.models import Book
try:
    book.delete()
    print("book deleted successfully")  
except Book.DoesNotExist:
    print("Book not found)

Expected output:
    book deleted successfully

