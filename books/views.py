from rest_framework import generics, filters, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book


class CreateBook(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class DeleteBook(generics.DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class FindBook(generics.ListAPIView):
    permission_classes = [AllowAny]
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ['name', 'author']
    queryset = Book.objects.all()
    serializer_class = BookSerializer







