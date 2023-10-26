from django.urls import path
from .views import BookListApi, book_list_view, BookDetailApiView, BookDeleteApi, BookUpdateApi, BookCreateApi, BookListCreateApi, \
BookDetailUpdateCreateApi

urlpatterns = [
    path('books/create', BookCreateApi.as_view(),),
    path('books/getpost', BookListCreateApi.as_view(),),
    path('books/<int:pk>/', BookDetailApiView.as_view(),),
    path('books/<int:pk>/getpost', BookDetailUpdateCreateApi.as_view(),),
    path('books/<int:pk>/delete/', BookDeleteApi.as_view(),),
    path('books/<int:pk>/update/', BookUpdateApi.as_view(),),
    path('', BookListApi.as_view(),),
    path('books/', book_list_view,)
]