# Generated by Django 3.2.3 on 2021-07-27 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('torneios', '0019_auto_20210726_1823'),
    ]

    operations = [
        migrations.CreateModel(
            name='Placar',
            fields=[
                ('placarId', models.AutoField(primary_key=True, serialize=False)),
                ('numeroSet', models.IntegerField()),
                ('numeroGame', models.IntegerField()),
                ('dataInclusao', models.DateTimeField(auto_now_add=True)),
                ('dataAtualizacao', models.DateTimeField(auto_now_add=True)),
                ('equipe', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='torneios.equipes')),
                ('jogo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='torneios.jogos')),
            ],
        ),
    ]