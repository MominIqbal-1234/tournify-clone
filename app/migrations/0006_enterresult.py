# Generated by Django 3.2.7 on 2023-10-30 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_createteam'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnterResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=255)),
                ('kill', models.CharField(max_length=255)),
                ('team_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.createteam')),
            ],
            options={
                'db_table': 'EnterResult',
            },
        ),
    ]
