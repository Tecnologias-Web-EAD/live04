"""live04 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path

from core.views import entrar, home
from cursos.views import curso_detalhes, curso_form

urlpatterns = [
    path('', home, name="home"),
    path('entrar/', entrar, name="entrar"),
    path('cursos/novo/', curso_form, name="curso_form"),
    path('cursos/<str:etiqueta>/', curso_detalhes, name="curso_detalhes")

]
