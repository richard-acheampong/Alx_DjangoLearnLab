from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView


urlpatterns = [
    path('books/', view= BookListView.as_view(), name= 'book-list'),
    path('books/<int:pk>/', view= BookDetailView.as_view(), name='book-detail')
    path('books/create/', view= BookCreateView.as_view(), name= 'book-create')
    path('book/update/<int:pk>/', view= BookUpdateView.as_view(), name= 'book-update')
    path('books/delete/<int:pk>/', view= BookDeleteView.as_view(), name= 'book-delete')
]