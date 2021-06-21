from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db.models import Q

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

    def perform_create(self, serializer):
        category = get_object_or_404(Category, id=self.request.data.get('category'))
        return serializer.save(category=category)


class SingleBookView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


class FilterAllView(ListAPIView):
    serializer_class = BooksSerializer

    def get_queryset(self):
        author = self.kwargs['author']
        name = self.kwargs['name']
        year = self.kwargs['year']
        return Book.objects.filter(
            Q(author__icontains=author) |
            Q(name__icontains=name) |
            Q(date_of_pub__year=year)
        )


# class FilterBookView(ListAPIView):
#     serializer_class = BooksSerializer
#
#     def get_queryset(self):
#         name = self.kwargs['name']
#         return Book.objects.filter(author__icontains=name)
