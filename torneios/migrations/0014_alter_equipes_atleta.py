# Generated by Django 3.2.3 on 2021-07-25 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atletas', '0012_auto_20210724_2244'),
        ('torneios', '0013_auto_20210724_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipes',
            name='atleta',
            field=models.ManyToManyField(related_name='atletas', to='atletas.Atletas', verbose_name='Atleta(s'),
        ),
    ]
