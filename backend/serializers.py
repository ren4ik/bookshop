from rest_framework import serializers

from catalog.models import Category, Book


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            'name',
            'slug',
            'category',
            'date_of_pub',
            'author',
            'image',
            'description',
            'price',
            'stock',
            'available'
        )