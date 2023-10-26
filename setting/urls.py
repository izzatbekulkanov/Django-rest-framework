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

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('books.urls'))
]
