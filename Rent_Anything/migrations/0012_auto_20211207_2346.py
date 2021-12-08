# Generated by Django 3.2.9 on 2021-12-08 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rent_Anything', '0011_items_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='items',
            name='phone',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='items',
            name='zip',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='items',
            name='img',
            field=models.ImageField(blank=True, default='img0.png', null=True, upload_to=''),
        ),
    ]