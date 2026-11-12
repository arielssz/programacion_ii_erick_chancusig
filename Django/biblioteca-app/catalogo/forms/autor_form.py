
from django import forms
from catalogo.models import Autor


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'nacionalidad']
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'nacionalidad': 'Nacionalidad',
        }
