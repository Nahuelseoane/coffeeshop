# Generated by Django 4.2.13 on 2024-07-11 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='orden',
            new_name='order',
        ),
    ]
