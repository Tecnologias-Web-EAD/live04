from django.db import models


class Curso(models.Model):

    nome = models.CharField('Nome', max_length=120, unique=True)
    sigla = models.CharField('Sigla', max_length=5, unique=True)
    etiqueta = models.SlugField('Etiqueta', null=True)
    descricao = models.TextField('Descrição', null=True)
    duracao = models.PositiveIntegerField('Duração')

    def __str__(self):
        return f'{self.nome} ({self.sigla})'
