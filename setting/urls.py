"""
Loyihani sozlash uchun URL konfiguratsiyasi.

`urlpatterns` roʻyxati URL manzillarini koʻrishlarga yoʻnaltiradi. Qo'shimcha ma'lumot uchun qarang:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Misollar:
Funktsiya ko'rinishlari
    1. Import qo‘shing: my_app import ko‘rinishlaridan
    2. URL namunalariga URL qo‘shing: path('', views.home, name='home')
Sinfga asoslangan ko'rinishlar
    1. Import qo‘shing: from other_app.views import Home
    2. Urlpatternsga URL qo‘shing: path('', Home.as_view(), name='home')
Shu jumladan boshqa URLconf
    1. include() funksiyasini import qiling: django.urls dan import include, path
    2. URL namunalariga URL qo‘shing: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#swagger drg_yash uchun urllar

schema_view = get_schema_view(
    openapi.Info(
        title="Book list Api",
        default_version='v1',
        description='Library demo project',
        terms_of_service='demo.com',
        contact=openapi.Contact(email='izzatbekulkanov@gmail.com'),
        license=openapi.License(name='demo licence')
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('books.urls')),

    #swagger uchun url
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
