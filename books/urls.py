from django.urls import path
from .views import CreateBook, FindBook, DeleteBook


urlpatterns = [
    path('create/', CreateBook.as_view()),
    path('search/', FindBook.as_view()),
    path('api/books/<int:pk>/', DeleteBook.as_view(), name='book-delete')
]
