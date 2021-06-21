from django.conf.urls import url
from django.urls import path, re_path
from .views import CategoryView, BookView, SingleBookView, SingleCategoryView

app_name = "backend"

urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('categories/<int:pk>/', SingleCategoryView.as_view()),
    path('books/', BookView.as_view()),
    path('books/<int:pk>/', SingleBookView.as_view()),
]