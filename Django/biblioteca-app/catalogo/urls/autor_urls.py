
from django.urls import path
from catalogo.views.autor_views import (
    autor_list,
    autor_create,
    autor_edit,
)

urlpatterns = [
    path('autores/', autor_list, name='autor_list'),
    path('autores/nuevo/', autor_create, name='create_autor'),
    path('autores/<int:pk>/editar/', autor_edit, name='autor_edit'),
]
