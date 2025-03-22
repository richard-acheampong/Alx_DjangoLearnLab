from django.urls import path
from django.contrib.auth import views
from . views import PostDeleteView, PostUpdateView, PostCreateView, RegisterView, ProfileView, Homeview, PostListView, PostDetailView

urlpatterns = [
    path('', Homeview.as_view(), name= 'home'),
    path('login/', views.LoginView.as_view(), name= 'login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name= 'register'),
    path('profile/', ProfileView.as_view(), name= 'profile'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-creat'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name= 'post-update'), 
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name= 'post-delete'),
]