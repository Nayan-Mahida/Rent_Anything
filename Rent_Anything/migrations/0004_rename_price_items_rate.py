# Generated by Django 3.2.9 on 2021-12-06 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rent_Anything', '0003_auto_20211203_1903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='price',
            new_name='rate',
        ),
    ]