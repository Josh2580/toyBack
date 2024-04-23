from django.test import TestCase
from django.utils import timezone
from myTelegramUser.models import TelegramUser
from toycoin.models import ToyCoin
from toycoin.serializers import ToyCoinSerializer, CreateToyCoinSerializer

class ToyCoinSerializerTest(TestCase):
    def setUp(self):
        # Creating a user instance
        self.user = TelegramUser.objects.create(
            username="user123",
            telegram_id="1234567890",
            language_code="en",
            currency="ADA"
        )
        self.toycoin_data = {
            'name': "TOY COIN",
            'quantity_mined': "100.00",
            'time_clicked': timezone.now()
        }

    def test_toycoin_serializer_with_valid_data(self):
        serializer = ToyCoinSerializer(data={**self.toycoin_data, 'user': self.user.id})
        self.assertTrue(serializer.is_valid())

    def test_create_toycoin_serializer_with_valid_data(self):
        data = {
            'name': "TOY COIN",
            'quantity_mined': "200.00",
            'time_clicked': timezone.now(),
            'telegram_id': self.user.telegram_id
        }
        serializer = CreateToyCoinSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        toycoin = serializer.save()
        self.assertEqual(ToyCoin.objects.count(), 1)
        self.assertEqual(toycoin.name, "TOY COIN")

    def test_create_toycoin_serializer_with_invalid_telegram_id(self):
        data = {
            'name': "TOY COIN",
            'quantity_mined': "200.00",
            'time_clicked': timezone.now(),
            'telegram_id': "invalid_id"
        }
        serializer = CreateToyCoinSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('telegram_id', serializer.errors)

    def test_toycoin_serializer_returns_expected_fields(self):
        toycoin = ToyCoin.objects.create(user=self.user, **self.toycoin_data)
        serializer = ToyCoinSerializer(toycoin)
        data = serializer.data
        self.assertEqual(set(data.keys()), {'id', 'user', 'name', 'quantity_mined', 'time_clicked', 'first_click', 'date_joined', 'mineral_extracted', 'launch_date'})
