from toycoin.models import ToyCoin
from rest_framework import serializers


class ToyCoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToyCoin
        fields = "__all__"