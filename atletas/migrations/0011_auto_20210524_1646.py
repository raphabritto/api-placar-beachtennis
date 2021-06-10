# Generated by Django 3.2.3 on 2021-05-24 19:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('atletas', '0010_atletas_cidade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atletas',
            old_name='data_ultima_modificacao',
            new_name='data_atualizacao',
        ),
        migrations.AlterField(
            model_name='atletas',
            name='apelido',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
