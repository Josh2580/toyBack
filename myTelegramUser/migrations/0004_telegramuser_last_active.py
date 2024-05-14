# Generated by Django 5.0.4 on 2024-05-14 09:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myTelegramUser', '0003_telegramuser_referrer'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='last_active',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
