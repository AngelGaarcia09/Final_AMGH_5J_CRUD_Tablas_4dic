# Generated by Django 5.1 on 2024-12-03 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='dnl',
            new_name='curp',
        ),
    ]
