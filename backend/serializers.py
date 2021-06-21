from rest_framework import serializers

from catalog.models import Category, Book


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', )


class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            'id',
            'name',
            'category',
            'year',
            'author',
            'image',
            'description',
            'price',
            'stock',
            'available'
        )