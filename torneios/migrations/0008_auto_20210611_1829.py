# Generated by Django 3.2.3 on 2021-06-11 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('torneios', '0007_torneiocategorias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='torneios',
            name='cidade',
        ),
        migrations.RemoveField(
            model_name='torneios',
            name='dataInicioInscricao',
        ),
        migrations.RemoveField(
            model_name='torneios',
            name='dataInicioTorneio',
        ),
        migrations.RemoveField(
            model_name='torneios',
            name='dataTerminoInscricao',
        ),
        migrations.RemoveField(
            model_name='torneios',
            name='dataTerminoTorneio',
        ),
        migrations.RemoveField(
            model_name='torneios',
            name='email',
        ),
        migrations.RemoveField(
            model_name='torneios',
            name='endereco',
        ),
        migrations.RemoveField(
            model_name='torneios',
            name='informacao',
        ),
        migrations.RemoveField(
            model_name='torneios',
            name='local',
        ),
        migrations.RemoveField(
            model_name='torneios',
            name='panfleto',
        ),
        migrations.RemoveField(
            model_name='torneios',
            name='responsavel',
        ),
        migrations.RemoveField(
            model_name='torneios',
            name='telefone',
        ),
    ]