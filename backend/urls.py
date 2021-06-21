from django.conf.urls import url
from django.urls import path, re_path
from .views import CategoryView, BookView, SingleBookView, SingleCategoryView, SingleProfileView, SingleUserView

from backend.views import UserAPI, UserListView, MyLoginView, ProfileListView

app_name = "backend"

urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('categories/<int:pk>/', SingleCategoryView.as_view()),
    path('books/', BookView.as_view()),
    path('books/<int:pk>/', SingleBookView.as_view()),
    path('user/registr/', UserAPI.as_view()),
    path('user/profiles/', ProfileListView.as_view()),
    path('user/users/', UserListView.as_view()),
    path('user/profiles/<int:pk>/', SingleProfileView.as_view()),
    path('user/users/<int:pk>/', SingleUserView.as_view()),
    path('user/users/login/', MyLoginView.as_view()),
]