# Generated by Django 5.1 on 2024-08-31 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmapp', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
