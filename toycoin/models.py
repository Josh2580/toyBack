from django.db import models
from django.utils import timezone
from myTelegramUser.models import TelegramUser



# Create your models here.



class ToyCoin(models.Model):
    user = models.OneToOneField(TelegramUser, related_name='user_coin', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(default="TOY COIN", max_length=20)
    quantity_mined = models.DecimalField(max_digits=10, default="100.00", decimal_places=2)
    time_clicked = models.DateTimeField()
    first_click = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    mineral_extracted = models.CharField(max_length=50, null=True, blank=True)
    extraction_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"