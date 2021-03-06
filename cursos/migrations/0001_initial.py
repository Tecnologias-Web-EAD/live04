# Generated by Django 2.2 on 2020-10-15 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120, unique=True, verbose_name='Nome')),
                ('sigla', models.CharField(max_length=5, unique=True, verbose_name='Sigla')),
                ('descricao', models.TextField(null=True, verbose_name='Descrição')),
                ('duracao', models.PositiveIntegerField(verbose_name='Duração')),
            ],
        ),
    ]
