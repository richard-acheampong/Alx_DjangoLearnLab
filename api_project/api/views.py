from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated

#Create your views here.
class BookList(ListAPIView):
    queryset = Book.objects.all()  # Fetch all books
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Fetch all books
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can access this view