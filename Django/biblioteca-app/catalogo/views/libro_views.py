from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from catalogo.forms.libro_form import LibroForm
from catalogo.models import Libro


@login_required
def libro_list(request):
    libros = Libro.objects.all()
    return render(request, 'catalogo/libros/libro_list.html', {'libros': libros})


@login_required
def libro_create(request):
    form = LibroForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Libro creado exitosamente.')
        return redirect('libro_list')
    return render(request, 'catalogo/libros/formulario.html', {'form': form, 'titulo': 'Nuevo libro'})


@login_required
def libro_edit(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    form = LibroForm(request.POST or None, instance=libro)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Libro actualizado exitosamente.')
        return redirect('libro_list')
    return render(request, 'catalogo/libros/formulario.html', {'form': form, 'titulo': 'Editar libro'})


@login_required
def libro_delete(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        messages.success(request, 'Libro eliminado exitosamente.')
        return redirect('libro_list')
    return render(request, 'catalogo/libros/confirmar_eliminar.html', {'libro': libro})
