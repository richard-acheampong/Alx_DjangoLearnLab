from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

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

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})  

# Helper function to check if the user is an admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Helper function to check if the user is a librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Helper function to check if the user is a member
def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view - only accessible by Admin users
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

# Librarian view - only accessible by Librarian users
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

# Member view - only accessible by Member users
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')

 