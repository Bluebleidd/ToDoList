# Generated by Django 5.1.4 on 2024-12-15 01:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('TO DO', 'To Do'), ('DOING', 'Doing'), ('DONE', 'Done')], max_length=10)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='app.board')),
            ],
        ),
    ]