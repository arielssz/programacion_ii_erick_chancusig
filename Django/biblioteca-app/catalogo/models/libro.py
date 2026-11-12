
from django.db import models
from .categoria import Categoria


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    fecha_publicacion = models.DateField()

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    isbn = models.CharField(
        max_length=13,
        blank=True,
        default=''
    )

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['titulo']
