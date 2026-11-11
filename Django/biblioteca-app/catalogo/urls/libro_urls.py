from django.urls import path
from catalogo.views.libro_views import libro_list, libro_create, libro_edit, libro_delete

urlpatterns = [
    path('libros/', libro_list, name='libro_list'),
    path('libros/nuevo/', libro_create, name='create_libro'),
    path('libros/<int:pk>/editar/', libro_edit, name='libro_edit'),
    path('libros/<int:pk>/eliminar/', libro_delete, name='libro_delete'),
]
