from django.db import models

# Create your models here.

class TelegramUser(models.Model):
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    telegram_id = models.CharField(unique=True, max_length=200)
    currency = models.CharField(max_length=50, default="ADA")
    


    def __str__(self):
        return self.username