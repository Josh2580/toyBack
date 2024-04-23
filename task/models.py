from django.db import models
# from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from myTelegramUser.models import TelegramUser

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


    def __str__(self):
        return f"Task {self.id} {self.completed}"
    
    class Meta:
        ordering = ["id"]