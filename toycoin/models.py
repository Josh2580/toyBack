from django.db import models
from django.utils import timezone
from myTelegramUser.models import TelegramUser
from django.db.models import Sum

# Create your models here.


class ToyCoin(models.Model):
    user = models.OneToOneField(TelegramUser, related_name='user_coin', on_delete=models.CASCADE)
    name = models.CharField(default="TOY COIN", max_length=20)
    quantity_mined = models.DecimalField(max_digits=10, default="100.00", decimal_places=2)
    time_clicked = models.DateTimeField()
    first_click = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    mineral_extracted = models.CharField(max_length=50, null=True, blank=True)
    launch_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.name}"

    
    @classmethod
    def get_total_quantity_mined(cls):
        result = cls.objects.aggregate(total_mined=Sum('quantity_mined'))
        return result['total_mined'] or 0  # Returning 0 if None

    
    def save(self, *args, **kwargs):
        # Enforce specific month, day, hour, minute, and second
        enforced_datetime = timezone.now().replace(
            month=8,  # January
            day=1,    # 1st of the month
            hour=0,   # 12 AM
            minute=0, # 00 minutes
            second=0, # 00 seconds
            microsecond=0  # Ensuring no microseconds
        )
        # Assign the enforced datetime to the field
        self.launch_date = enforced_datetime
        super().save(*args, **kwargs)