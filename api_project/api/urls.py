from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import BookList
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

#create router and register our viewset
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book_all')

urlpatterns = [
    # path('books/', BookList.as_view(), name='book-list'),
    path(' ', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]