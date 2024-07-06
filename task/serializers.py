from rest_framework import serializers
# from .models import TelegramUser, Order
from .models import Task, AutoBot

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"



class TaskSerializerSecond(serializers.ModelSerializer):

    class Meta:
        model = Task
        # fields = "__all__"
        exclude = ["user"]



class AutoBotSerializer(serializers.ModelSerializer):

    class Meta:
        model = AutoBot
        fields = "__all__"