from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.

class TelegramUser(models.Model):
    username = models.CharField(max_length=355, null=True, blank=True)
    first_name = models.CharField(max_length=355, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    telegram_id = models.CharField(unique=True, max_length=200)
    language_code = models.CharField(max_length=255, default="en")
    currency = models.CharField(max_length=50, default="ADA")
    referrer = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='referred_users')
    last_active = models.DateTimeField()
    

    def __str__(self):
        return f"{self.telegram_id}"
    

    @classmethod
    def get_online_users(cls):
        one_hour_ago = timezone.now() - timedelta(hours=2)
        return cls.objects.filter(last_active__gte=one_hour_ago).count()
    
    @classmethod
    def get_daily_users(cls):
        one_day_ago = timezone.now() - timedelta(days=1)
        return cls.objects.filter(last_active__gte=one_day_ago).count()
    
    @classmethod
    def get_total_users(cls):
        return cls.objects.all().count()

