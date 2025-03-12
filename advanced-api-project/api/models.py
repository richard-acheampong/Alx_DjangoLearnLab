from django.db import models

# Create your models here.
#author models to store author details
class Author(models.Model):
    name = models.CharField(max_length=100)
   
    def __str__(self):
        return self.name

#book model to store book details    
class Book(models.Model):
    title = models.CharField(max_length=150)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)