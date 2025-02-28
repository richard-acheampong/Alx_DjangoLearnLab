create a book instance
#1. import Book model from app
   command: 
    from bookshelf.models import Book
#2. create book instance
    command:
     book = Book.objects.create(title= "1984", author= "George Orwell", publication_year= 1949)

     print(book)

Expected output:
    Book object(1)

