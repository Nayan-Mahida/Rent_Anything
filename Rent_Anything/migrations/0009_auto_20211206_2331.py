# Generated by Django 3.2.9 on 2021-12-07 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rent_Anything', '0008_alter_items_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to='images')),
            ],
        ),
        migrations.RemoveField(
            model_name='items',
            name='img',
        ),
    ]
