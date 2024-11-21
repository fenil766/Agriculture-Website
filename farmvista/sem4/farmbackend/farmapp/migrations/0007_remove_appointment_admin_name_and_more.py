# Generated by Django 5.1 on 2024-09-07 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmapp', '0006_appointment_appointment_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='admin_name',
        ),
        migrations.RemoveField(
            model_name='appointment_details',
            name='admin_name',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='appointment_details',
            name='user_name',
        ),
        migrations.DeleteModel(
            name='ADMIN',
        ),
        migrations.DeleteModel(
            name='APPOINTMENT',
        ),
        migrations.DeleteModel(
            name='APPOINTMENT_DETAILS',
        ),
    ]
