# Generated by Django 5.1.4 on 2024-12-10 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectCore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='is_completed',
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('To Do', 'Do zrobienia'), ('Doing', 'W trakcie'), ('Done', 'Zrobione')], default='To Do', max_length=20),
        ),
    ]
