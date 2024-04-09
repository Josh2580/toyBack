from toycoin.models import ToyCoin
from rest_framework import serializers
from myTelegramUser.models import TelegramUser

class ToyCoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToyCoin
        fields ="__all__"


class CreateToyCoinSerializer(serializers.ModelSerializer):
    # Optionally include the telegram_id in the serializer for validation or display
    # This field is read-only because we don't want it to be included in the validated_data
    # and is not a model field of ToyCoin; it's used for lookup in the view.
    telegram_id = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = ToyCoin
        fields = ['id', 'name', 'quantity_mined', 'time_clicked', 'telegram_id']
        read_only_fields = ['id']  # Assuming 'id' is an auto-increment field

    def create(self, validated_data):
        """
        Overriding the create method is optional in this context because the actual saving logic
        and setting of the 'user' based on 'telegram_id' is handled in the view's perform_create method.
        If you need to perform additional manipulation on instance creation, you can do it here.
        Remember to remove 'telegram_id' from validated_data since it's not a model field of ToyCoin.
        """
        validated_data.pop('telegram_id', None)  # Remove telegram_id as it's not a model field

        # Instance creation logic
        toycoin = super().create(validated_data)

        return toycoin

    def validate_telegram_id(self, value):
        """
        You can include validation for telegram_id if necessary, for example, to check
        if the TelegramUser exists here, but it's also checked in the view.
        """
        if not TelegramUser.objects.filter(telegram_id=value).exists():
            raise serializers.ValidationError("TelegramUser with this telegram_id does not exist.")
        return value
