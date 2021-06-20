from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from catalog.models import Category, Book
from .serializers import CategoriesSerializer, BooksSerializer


class CategoryView(APIView):
    """CRUD API for Category"""
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response({"categories": serializer.data})

    def post(self, request):
        category = request.data.get('category')
        # Create an article from the above data
        serializer = CategoriesSerializer(data=category)
        if serializer.is_valid(raise_exception=True):
            category_saved = serializer.save()
        return Response({"success": "Category '{}' created successfully".format(category_saved.name)})

    def put(self, request, slug):
        saved_category = get_object_or_404(Category.objects.all(), slug=slug)
        data = request.data.get('category')
        serializer = CategoriesSerializer(instance=saved_category, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            category_saved = serializer.save()
        return Response({
            "success": "Category '{}' updated successfully".format(category_saved.name)
        })

    def delete(self, request, slug):
        # Get object with this pk
        category = get_object_or_404(Category.objects.all(), slug=slug)
        category.delete()
        return Response({
            "message": "Category with slug `{}` has been deleted.".format(slug)
        }, status=204)


class BookView(ListModelMixin, GenericAPIView):
    """CRUD API for Book"""


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request):
        book = request.data.get('book')
        # Create an article from the above data
        serializer = BooksSerializer(data=book)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response({"success": "Category '{}' created successfully".format(book_saved.name)})

    def put(self, request, slug):
        saved_book = get_object_or_404(Book.objects.all(), slug=slug)
        data = request.data.get('book')
        serializer = BooksSerializer(instance=saved_book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response({
            "success": "Book '{}' updated successfully".format(book_saved.name)
        })

    def delete(self, request, slug):
        # Get object with this pk
        book = get_object_or_404(Book.objects.all(), slug=slug)
        book.delete()
        return Response({
            "message": "Book with slug `{}` has been deleted.".format(slug)
        }, status=204)


