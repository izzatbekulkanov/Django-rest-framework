from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics

# Create your views here.
#Barcha Book modeliga tegishli jadvaldagi malumotlarni dictionary ko'rinishida chiqarib beradi
class BookListApi (generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
#Book modelidagi elementlar ichidan id siga qarab detail page chiqarib beradi
class BookDetailApiView (generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
#Book modelidagi elementlar ichidan id siga qarab Delete qilib beradi
class BookDeleteApi(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
#Book modelidagi elementlar ichidan id siga qarab Update qilib beradi
class BookUpdateApi(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
#django rest frameworki asosida api orqali yangi Book modeliga tegishli element yaratadi
class BookCreateApi(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
#django rest framework orqali Ham GET ham POST requestlarga ruxsat berilgan holda view quyidagicha yaratiladi
class BookListCreateApi(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
#django rest framework orqali bir elementni Ham GET ham POST ham DELETE requestlarga ruxsat berilgan holda view quyidagicha yaratiladi
class BookDetailUpdateCreateApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer








#Barcha Book modeliga tegishli jadvaldagi malumotlarni funksiya asosida dictionary ko'rinishida chiqarib beradi
@api_view(['GET'])
def book_list_view(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)



