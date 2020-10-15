from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

from cursos.models import Curso

def home(request):
    cursos = Curso.objects.all()
    contexto = {
        'cursos': cursos
    }
    return render(request, 'index.html', contexto)


def entrar(request):

    if request.method == 'POST':
        print('é um POST')
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(request, username=usuario, password=senha)
        if user:
            login(request, user)
            return redirect('home')
        else: 
            print('Usuário ou senha incorretos!')

    return render(request, 'entrar.html')
