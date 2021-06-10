# Generated by Django 3.2.3 on 2021-06-03 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneios', '0004_rename_somentedupla_generocategorias_somenteduplas'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCategorias',
            fields=[
                ('tipoId', models.AutoField(primary_key=True, serialize=False)),
                ('nomeTipo', models.CharField(max_length=50)),
                ('quantidadeAtletas', models.SmallIntegerField()),
                ('ativo', models.BooleanField(default=True)),
                ('dataInclusao', models.DateTimeField(auto_now_add=True)),
                ('dataAtualizacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='generocategorias',
            name='somenteDuplas',
        ),
    ]
