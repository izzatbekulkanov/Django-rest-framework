from django.contrib.sites import requests
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, request, status

#local kutubhonalar
from .models import Book
from .serializers import BookSerializer

# Create your views here.
#Barcha Book modeliga tegishli jadvaldagi malumotlarni dictionary ko'rinishida chiqarib beradi Tayyor ListAPIView orqali
# class BookListApi (generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#Barcha Book modeliga tegishli jadvaldagi malumotlarni dictionary ko'rinishida chiqarib beradi APIView orqali
class BookListApi(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            'status': f"Returned {len(books)} books",
            'books': serializer_data
        }

        return Response(data)
    # Swaggerda sarlavha sifatida nimaligini chiqarish uchun qo'llaniladi
    @swagger_auto_schema(
        operation_description="Kitoblar ro'yhatini chiqarish",
        operation_summary="Kitoblar ro'yxatini chiqarish uchun",
        operation_id="*",
        tags=["Frontend API"],
        responses={200: BookSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

#Book modelidagi elementlar ichidan id siga qarab detail page chiqarib beradi
class BookDetailApiView (generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
#Book modelidagi elementlar ichidan id siga qarab detail page chiqarib beradi ApiView orqali
class BookDetailApiView (generics.RetrieveAPIView):
    def get(self, requeset, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data

            data = {
                'status': "Successfull",
                'book': serializer_data
            }
            return Response(data)
        except Exception:
            return Response(
                {"status": "ERROR Bunday ma'lumot yo'q"}
            )

#Book modelidagi elementlar ichidan id siga qarab Delete qilib beradi
# class BookDeleteApi(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#Book modelidagi elementlar ichidan id siga qarab Delete qilib beradi ApiView orqali
class BookDeleteApi(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response({
                "status": True,
                "Message": "Successfull delete on book"
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                "status": False,
                "Message": "Book is not delete"
            }, status=status.HTTP_400_BAD_REQUEST)

#Book modelidagi elementlar ichidan id siga qarab Update qilib beradi
# class BookUpdateApi(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#Book modelidagi elementlar ichidan id siga qarab Update qilib beradi ApiView orqali
class BookUpdateApi(APIView):
    #Bu yerda try: orqali emas rest frameworkning get_object_or_404 orqali try qilingan
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response({
            "status": True,
            "messages": f"Book {book_saved.author} updated successfully"
        })


#django rest frameworki asosida api orqali yangi Book modeliga tegishli element yaratadi CreateAPIView yordamida
# class BookCreateApi(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#django rest frameworki asosida api orqali yangi Book modeliga tegishli element yaratadi APIVEIW yordamida
class BookCreateApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': "Books are saved to the database",
                'books': data
            }
            return Response(data)
        else:
            return Response(
                {
                    "status": False,
                    "message": "Serializer is not valid"
                }, status=status.HTTP_400_BAD_REQUEST
            )

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



