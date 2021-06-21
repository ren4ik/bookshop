from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .service import BookFilter
from django_filters.rest_framework import DjangoFilterBackend

from catalog.models import Category, Book
from .serializers import CategoriesSerializer, BooksSerializer


class CategoryView(ListCreateAPIView):
    """CRUD API for Category"""
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


class SingleCategoryView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


class BookView(ListCreateAPIView):
    """CRUD API for Book"""
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookFilter

    def perform_create(self, serializer):
        category = get_object_or_404(Category, id=self.request.data.get('category'))
        return serializer.save(category=category)


class SingleBookView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


