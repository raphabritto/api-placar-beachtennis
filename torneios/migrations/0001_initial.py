# Generated by Django 3.1.2 on 2020-10-31 01:55

from django.db import migrations, models
import torneios.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Torneios',
            fields=[
                ('torneio_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('data_inicio', models.DateField()),
                ('data_termino', models.DateField()),
                ('uf', models.CharField(max_length=2)),
                ('pais', models.CharField(max_length=60)),
                ('cidade', models.CharField(max_length=60)),
                ('local', models.CharField(max_length=80)),
                ('endereco', models.CharField(max_length=120)),
                ('responsavel', models.CharField(max_length=60)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('observacao', models.TextField(max_length=1000, null=True)),
                ('panfleto', models.ImageField(blank=True, null=True, upload_to=torneios.models.upload_panfleto_torneio)),
                ('data_inclusao', models.DateTimeField(auto_now_add=True)),
                ('data_ultima_modificacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
