# Generated by Django 5.1 on 2024-09-07 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmapp', '0009_remove_appointment_admin_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ADMIN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('passward', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='APPOINTMENT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('appointment_date', models.DateTimeField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='APPOINTMENT_DETAILS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('ratio', models.IntegerField()),
                ('condition', models.CharField(max_length=100)),
                ('recommendation', models.CharField(max_length=1000)),
                ('next_c', models.CharField(max_length=100)),
            ],
        ),
    ]
