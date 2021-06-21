from django.conf.urls import url
from django.urls import path, re_path
from .views import CategoryView, BookView, SingleBookView, SingleCategoryView, FilterAllView

app_name = "backend"

urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('categories/<int:pk>/', SingleCategoryView.as_view()),
    path('books/', BookView.as_view()),
    path('books/<int:pk>/', SingleBookView.as_view()),
    re_path(r'^books/filter/(?P<author>\w+)&(?P<name>\w+)&(?P<year>\d{4})/$', FilterAllView.as_view())
]