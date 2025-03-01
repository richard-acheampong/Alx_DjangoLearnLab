from django.contrib import admin
from django.contrib.auth.views import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .views import list_books, LibraryDetailView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="authentication/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="logout")),
    
]