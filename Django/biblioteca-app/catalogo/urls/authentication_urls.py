from django.urls import path
from catalogo.views.authentication_views import BibliotecaloginView, Bibliotecalogout_view

urlpatterns = [
    path('login/', BibliotecaloginView.as_view(), name='login'),
    path('logout/', Bibliotecalogout_view.as_view(), name='logout'),
]
