from rest_framework import serializers
# from .models import TelegramUser, Order
from .models import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"

