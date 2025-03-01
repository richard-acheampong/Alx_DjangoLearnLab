from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic import DetailView

# Create your views here.
def list_books(request):
    """Retrieves all books and renders a template displaying the list."""
    books = Book.objects.all()  # Fetch all book instances from the database
    context = {'books': books}  # Create a context dictionary with book list
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
    
    def get_context_data(self, **kwargs):
        """Extend context to include books in the library."""
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()  # Fetch all books related to the library
        return context
   