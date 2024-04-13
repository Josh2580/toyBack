from django.db import models
from myTelegramUser.models import TelegramUser

# Create your models here.
class Task(models.Model):
    user = models.ManyToManyField(TelegramUser, related_name='user_task', blank=True )
    task = models.CharField(default="The Users Task", max_length=1050)
    time_clicked = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} Task {self.id} {self.completed}"
    
    class Meta:
        ordering = ["id"]