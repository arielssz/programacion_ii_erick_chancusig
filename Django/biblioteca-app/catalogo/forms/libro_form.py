
from django import forms
from catalogo.models import Libro


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro

        fields = [
            'titulo',
            'autor',
            'fecha_publicacion',
            'categoria',
            'isbn'
        ]

        widgets = {
            'titulo': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'autor': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'fecha_publicacion': forms.DateInput(
                attrs={
                    'class': 'date',
                    'type': 'date'
                },
                format='%Y-%m-%d'
            ),
            'categoria': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'isbn': forms.TextInput(
                attrs={'class': 'form-control'}
            )
        }

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')

        if not titulo:
            raise forms.ValidationError(
                'El título es obligatorio.'
            )

        return titulo

    def clean_autor(self):
        autor = self.cleaned_data.get('autor')

        if not autor:
            raise forms.ValidationError(
                'El autor es obligatorio.'
            )

        return autor

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')

        if not isbn:
            return isbn

        if (
            len(isbn) != 13
            or not isbn.isascii()
            or not isbn.isdigit()
        ):
            raise forms.ValidationError(
                'El ISBN debe contener 13 dígitos.'
            )

        return isbn
