# Generated by Django 3.2.3 on 2021-06-03 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('torneios', '0003_rename_dupla_generocategorias_somentedupla'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generocategorias',
            old_name='somenteDupla',
            new_name='somenteDuplas',
        ),
    ]