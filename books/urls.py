from django.urls import path
from rest_framework.routers import SimpleRouter


#local viewlar
from .views import BookListApi, book_list_view, BookDetailApiView, BookDeleteApi, BookUpdateApi, BookCreateApiView, BookListCreateApi, \
BookDetailUpdateCreateApi, BookViewSet

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns = [
    # path('books/create', BookCreateApiView.as_view(),),
    # path('books/getpost', BookListCreateApi.as_view(),),
    # path('books/<int:pk>/', BookDetailApiView.as_view(),),
    # path('books/<int:pk>/getpost', BookDetailUpdateCreateApi.as_view(),),
    # path('books/<int:pk>/delete/', BookDeleteApi.as_view(),),
    # path('books/<int:pk>/update/', BookUpdateApi.as_view(),),
    # path('books/api/', BookListApi.as_view(),),
    # path('books/', book_list_view,)
]
urlpatterns += router.urls