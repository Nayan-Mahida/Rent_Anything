# Generated by Django 3.2.9 on 2021-12-07 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rent_Anything', '0009_auto_20211206_2331'),
    ]

    operations = [
        migrations.DeleteModel(
            name='image',
        ),
        migrations.AddField(
            model_name='items',
            name='img',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
