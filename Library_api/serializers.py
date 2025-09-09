from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'

class BookCostomSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    author=serializers.CharField(max_length=100)
    published_year=serializers.IntegerField()


# Input serializer (search by name)
class BookSearchSerializer(serializers.Serializer):
    name = serializers.CharField()

class BookDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    author = serializers.CharField()
    published_year = serializers.IntegerField()

#this is serializer