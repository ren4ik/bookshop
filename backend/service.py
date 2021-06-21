from django_filters import rest_framework as filters

from catalog.models import Book


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class BookFilter(filters.FilterSet):
    name = CharFilterInFilter(field_name='name', lookup_expr='in')
    author = CharFilterInFilter(field_name='author', lookup_expr='in')
    year = filters.RangeFilter(field_name='year')
    price = filters.RangeFilter()

    class Meta:
        model = Book
        fields = ['name', 'author', 'year', 'price']
