# Generated by Django 5.1 on 2024-08-31 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmapp', '0004_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='PRODUCT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='media/')),
                ('categorie', models.CharField(max_length=100)),
            ],
        ),
    ]
