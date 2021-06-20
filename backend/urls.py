from django.urls import path
from .views import CategoryView, BookView, SingleBookView

app_name = "backend"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('categories/<slug:slug>', CategoryView.as_view()),
    path('books/', BookView.as_view()),
    path('books/<int:pk>/', SingleBookView.as_view())
]