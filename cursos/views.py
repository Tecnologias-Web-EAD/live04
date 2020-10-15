from django.shortcuts import render, redirect

from cursos.forms import CursoForm
from cursos.models import Curso

def curso_detalhes(request, etiqueta):
    curso = Curso.objects.get(etiqueta=etiqueta)
    contexto = {
        'curso': curso
    }
    return render(request, 'cursos/curso.html', contexto)

def curso_form(request):
    
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else: 
        form = CursoForm()
    
    contexto = {
        'form': form
    }
    return render(request, 'cursos/form.html', contexto)