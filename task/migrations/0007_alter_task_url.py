# Generated by Django 5.0.4 on 2024-04-22 09:03

import task.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_alter_task_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='url',
            field=models.CharField(max_length=1050, validators=[task.models.validate_twitter_url]),
        ),
    ]
