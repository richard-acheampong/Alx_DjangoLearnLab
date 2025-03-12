from rest_framework import serializers
from .models import Author, Book
from datetime import date

#book serializer to serialize and deserialize book data
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    #validation method to ensure publication year is not in the future
    def validation(self, data):
        if data["publication_year"] > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future")
        return data

#author serializer to serialize author data
class AuthorSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ["id", "name", "book"]