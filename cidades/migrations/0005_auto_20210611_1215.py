# Generated by Django 3.2.3 on 2021-06-11 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cidades', '0004_cidades_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cidades',
            old_name='cidade_id',
            new_name='cidadeId',
        ),
        migrations.RenameField(
            model_name='cidades',
            old_name='nome',
            new_name='nomeCidade',
        ),
        migrations.RenameField(
            model_name='estados',
            old_name='estado_id',
            new_name='estadoId',
        ),
        migrations.RenameField(
            model_name='estados',
            old_name='nome',
            new_name='nomeEstado',
        ),
        migrations.RenameField(
            model_name='estados',
            old_name='sigla',
            new_name='siglaEstado',
        ),
        migrations.RenameField(
            model_name='paises',
            old_name='nome',
            new_name='nomePais',
        ),
        migrations.RenameField(
            model_name='paises',
            old_name='pais_id',
            new_name='paisId',
        ),
        migrations.RenameField(
            model_name='paises',
            old_name='sigla',
            new_name='siglaPais',
        ),
        migrations.RemoveField(
            model_name='cidades',
            name='data_inclusao',
        ),
        migrations.RemoveField(
            model_name='cidades',
            name='data_ultima_modificacao',
        ),
        migrations.RemoveField(
            model_name='cidades',
            name='sigla',
        ),
        migrations.RemoveField(
            model_name='estados',
            name='bandeira',
        ),
        migrations.RemoveField(
            model_name='estados',
            name='data_inclusao',
        ),
        migrations.RemoveField(
            model_name='estados',
            name='data_ultima_modificacao',
        ),
        migrations.RemoveField(
            model_name='paises',
            name='bandeira',
        ),
        migrations.RemoveField(
            model_name='paises',
            name='data_inclusao',
        ),
        migrations.RemoveField(
            model_name='paises',
            name='data_ultima_modificacao',
        ),
    ]