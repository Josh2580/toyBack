from rest_framework import serializers
# from .models import TelegramUser, Order
from toycoin.models import ToyCoin

class TelegramUserSerializer(serializers.ModelSerializer):
    user_coin = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = ToyCoin
        fields = ['id', 'username', 'first_name', 'last_name', 'telegram_id', 'user_coin']
        # fields = ['id', 'username', 'first_name', 'last_name', 'telegram_id']


# class OrderSerializer(serializers.ModelSerializer):
#     user = serializers.ReadOnlyField(source="user.id")

#     class Meta:
#         model = Order
#         fields = "__all__"