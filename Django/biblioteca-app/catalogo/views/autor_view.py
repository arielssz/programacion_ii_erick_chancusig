
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from catalogo.forms.autor_form import AutorForm
from catalogo.models import Autor


@login_required
def autor_list(request):
    autores = Autor.objects.all()
    return render(
        request,
        'catalogo/autores/autor_list.html',
        {'autores': autores}
    )


@login_required
def autor_create(request):
    form = AutorForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Autor creado exitosamente.')
        return redirect('autor_list')

    return render(
        request,
        'catalogo/autores/formulario.html',
        {'form': form, 'titulo': 'Nuevo autor'}
    )


@login_required
def autor_edit(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    form = AutorForm(request.POST or None, instance=autor)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Autor actualizado exitosamente.')
        return redirect('autor_list')

    return render(
        request,
        'catalogo/autores/formulario.html',
        {'form': form, 'titulo': 'Editar autor'}
    )
