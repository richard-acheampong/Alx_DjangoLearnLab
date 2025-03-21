from django.urls import path
from django.contrib.auth import views
from . views import RegisterView, ProfileView, Homeview

urlpatterns = [
    path('', Homeview.as_view(), name= 'home'),
    path('login/', views.LoginView.as_view(), name= 'login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name= 'register'),
    path('profile/', ProfileView.as_view(), name= 'profile'), 
]