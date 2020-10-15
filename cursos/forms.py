from django import forms

from cursos.models import Curso

class CursoForm(forms.ModelForm):

    class Meta:
        model = Curso
        fields = ['nome', 'etiqueta', 'sigla', 'duracao', 'descricao']
