# Generated by Django 3.2.7 on 2023-10-30 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_createtournament_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createtournament',
            name='additional_information',
        ),
    ]
