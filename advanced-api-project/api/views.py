from django.shortcuts import render
from rest_framework import generics
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import BookFilter
from rest_framework.filters import SearchFilter, OrderingFilter as filters_OrderingFilter


# Create your views here.
#BookListView for retrieving all books
class BookListView(generics.ListAPIView):
    """
    API View to retrieve a list of books.

    - **GET**: Returns a list of all books.
    - **Permissions**: Read-only for unauthenticated users; authenticated users can create books.
    """
    queryset = Book.objects.all()  
    serializer_class = BookSerializer # Serialize using the BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Allow read only access to unauthenticated users
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  # Configure the filter backends
    filterset_fields = ['title', 'author'] # Allow filtering by title, publication_year, and author
    #filter_class = BookFilter
    search_fields = ['title', 'author'] # Enable searching by title and author (remove publication_year for search)
    ordering_fields = ['title', 'author', 'publication_year'] # Allow ordering by title, author, or publication_year
    ordering = ['title'] # Default ordering by title

#BookDetailView for retrieving a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    API View to retrieve a single book by ID.

    - **GET**: Retrieve a book by its ID.
    - **Permissions**: Read-only for unauthenticated users; authenticated users can modify or delete.
    """
    queryset = Book.objects.all() #Retrieve all Book objects
    serializer_class = BookSerializer # Serialize using the BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Allow read only access to unauthenticated users

#BookCreateView for adding a new book
class BookCreateView(generics.CreateAPIView):
    """
    API view to create a new book.

    - **POST**: Create a book (only for authenticated users).
    - **Custom Validation**: Prevents adding duplicate books (same title & author).
    - **Permissions**: Only authenticated users can create books.
    """
    queryset = Book.objects.all() # Saves a new Book instance
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Restrict access to only authenticated users

    def perform_create(self, serializer):
        # Custom validation: Check if the book already exists before saving
        title = serializer.validated_data.get("title")
        author = serializer.validated_data.get("author")

        if Book.objects.filter(title=title, author=author).exists():
            return Response(
                {"error": "This book already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save()  # If validation passes, save the book

#BookUpdateView for modifying an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    API view to update an existing book.

    - **PUT/PATCH**: Update book details (only for authenticated users).
    - **Custom Validation**: Prevents modifying a book to duplicate an existing one.
    - **Permissions**: Only authenticated users can update books.
    """
    queryset = Book.objects.all() # Retrieve Book to update
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Restrict access to only authenticated users

    def perform_update(self, serializer):
        # Custom validation: Prevent duplicate books
        title = serializer.validated_data.get("title")
        author = serializer.validated_data.get("author")

        if Book.objects.filter(title=title, author=author).exists():
            return Response(
                {"error": "Another book with the same title and author already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save()  # Save the updated book if validation passes

#BookDeleteView for removing a book
class BookDeleteView(generics.DestroyAPIView):
    """
    API view to delete a book.

    - **DELETE**: Remove a book by ID (only for authenticated users).
    - **Permissions**: Only authenticated users can delete books.
    """
    queryset = Book.objects.all() # Retrieve a Book object to delete
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Restrict access to only authenticated users

