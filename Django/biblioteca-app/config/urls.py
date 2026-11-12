from django.contrib import admin
from django.urls import include, path
from catalogo.views.home_view import home
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('catalogo/', include('catalogo.urls.categoria_urls')),
    path('catalogo/', include('catalogo.urls.libro_urls')),
    path('cuentas/', include('catalogo.urls.authentication_urls')),
    path('catalogo/', include('catalogo.urls.autor_urls')),
    
]
