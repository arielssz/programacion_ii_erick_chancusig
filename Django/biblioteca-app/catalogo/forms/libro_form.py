from django import forms
from catalogo.models import Libro


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'fecha_publicacion']
        widgets = {'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')}
