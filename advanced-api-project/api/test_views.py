from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book, Author
from django.urls import reverse
from rest_framework.test import APIClient
import json




class BookTest(TestCase):
    def setUp(self):
        #create a test user
        self.user = User.objects.create_user(username= "testuser", password= "password124")

        #create author
        self.author1 = Author.objects.create(name="Test Author")
        self.author2 = Author.objects.create(name= "Test Author 2")

        #create book
        self.book = Book.objects.create(
            title = "Text book",
            publication_year= 2024,
            author = self.author1
        )

    
   
    def test_retrieve_all_books(self):
        print("testing retrieving all books")
        """
        Test retrieving a list of books
        """
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Text book")

    def test_retrieve_single_book(self):
        print("testing retrieving single book")
        """
        Test retrieving a single book
        """
        url = reverse("book-detail", kwargs={"pk": self.book.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["author"], 1)

    def test_create_book_authenticated(self):
        print("testing create book by authenticated user")
        """
        Test updating a new book
        """
        self.client.login(username= "testuser", password="password124")
        data = {
            "title": "Brave New World",
            "publication_year" :2025,
            "author" : self.author2.id
        }
        url = reverse("book-create")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    
    def test_create_book_unauthenticated(self):
        print("testing create book by unauthenticated user")
        """
        Test creating a new book by unauthenticated user
        """
        data = {
            "title": "Brave New Life",
            "publication_year" :2025,
            "author" : self.author1.id
        }
        url = reverse("book-create")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        

    def test_update_book_authenticated(self):
        print("testing update book by authenticated user")
        """
        Test updating a book by authenticated user
        """
        # self.client.login(username= "testuser", password="password124")
        client = APIClient()
        client.force_authenticate(user=self.user)

        data = {
            "title": "Brave New Realm",
            "publication_year" :2024,
            "author" : self.author1.id
        }

        url = reverse("book-update", kwargs={"pk": self.book.id})
        response = client.patch(url, data=json.dumps(data), content_type= "application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.book.refresh_from_db()
        # self.assertEqual(self.book.title, "Brave New Realm")
        # self.assertEqual(self.book.author, self.author2)
        # self.assertEqual(self.book.publication_year, 2025)
        # self.assertEqual(Book.objects.count(), 1)
        
    
    def test_update_book_unauthenticated(self):
        print("Testing update book by unauthenticated user")
        """
        Test updating a book by unauthenticated user
        """
        data = {
            "title": "Brave New Realm",
            "publication_year" :2025,
            "author" : self.author2.id
        }
        url = reverse("book-update", kwargs={"pk": self.book.id})
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_deleting_book_authenticated(self):
        print("Testing delete book by authenticated user")
        """
        Test deleting a book by authenticated user
        """
        self.client.login(username= "testuser", password="password124")
        url = reverse("book-delete", kwargs={"pk": self.book.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
    
    def test_deleting_book_unauthenticated(self):
        print("Testing delete book by unauthenticated user")
        """
        Test deleting a book by unauthenticated user
        """
        url = reverse("book-delete", kwargs={"pk": self.book.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    




