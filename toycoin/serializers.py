from toycoin.models import ToyCoin
from rest_framework import serializers
from myTelegramUser.models import TelegramUser

class ToyCoinSerializer(serializers.ModelSerializer):
    get_total_quantity_mined = serializers.CharField(read_only=True)
    get_total_users = serializers.IntegerField(read_only=True)
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
        telegram_id = validated_data.pop('telegram_id', None)  # Remove the telegram_id
        # Remove user if it exists in validated_data to prevent the error
        validated_data.pop('user', None)

        # Retrieve the user based on telegram_id or raise an error if not found
        user = TelegramUser.objects.filter(telegram_id=telegram_id).first()
        if not user:
            raise serializers.ValidationError("No TelegramUser found with this telegram_id.")

        # Create the ToyCoin instance with the user
        toycoin = ToyCoin.objects.create(user=user, **validated_data)
        return toycoin


    def validate_telegram_id(self, value):
        """
        You can include validation for telegram_id if necessary, for example, to check
        if the TelegramUser exists here, but it's also checked in the view.
        """
        if not TelegramUser.objects.filter(telegram_id=value).exists():
            raise serializers.ValidationError("TelegramUser with this telegram_id does not exist.")
        return value
