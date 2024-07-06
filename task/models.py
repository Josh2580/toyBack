from django.db import models
# from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from myTelegramUser.models import TelegramUser
from django.utils import timezone

# Validate the url
def validate_twitter_url(value):
    if not (value.startswith("http://") or value.startswith("https://") or value.startswith("twitter://")):
        raise ValidationError("Invalid URL: Must start with http://, https://, or twitter://.")


# Create your models here.
class Task(models.Model):
    user = models.ManyToManyField(TelegramUser, related_name='user_task', blank=True )
    task = models.CharField(default="The Users Task", max_length=1050)
    quantity = models.IntegerField(default=250)
    url = models.CharField(max_length=1050, validators=[validate_twitter_url])
    completed = models.BooleanField(default=False)
    group_id = models.CharField(max_length=255)


    def __str__(self):
        return f"Task {self.id} {self.completed}"
    
    class Meta:
        ordering = ["id"]



class AutoBot(models.Model):
    user = models.OneToOneField(TelegramUser, related_name='user_bot', on_delete=models.CASCADE, blank=True, null=True )
    activated = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    time = models.DateTimeField(default=timezone.now)
    duration = models.DurationField(null=True, blank=True)

    def __str__(self):
        return f"{self.id} ID: {self.user} Free Auto-Bot is {self.activated}"

