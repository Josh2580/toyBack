# Generated by Django 5.0.4 on 2024-05-20 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_alter_task_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='group_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]