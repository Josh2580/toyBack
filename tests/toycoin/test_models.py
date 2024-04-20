from django.test import TestCase
from django.utils import timezone
from myTelegramUser.models import TelegramUser
from toycoin.models import ToyCoin

class ToyCoinModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a TelegramUser instance
        cls.user = TelegramUser.objects.create(
            username="user123",
            telegram_id="1234567890",
            language_code="en",
            currency="ADA"
        )

        # Create a ToyCoin instance
        cls.toy_coin = ToyCoin.objects.create(
            user=cls.user,
            time_clicked=timezone.now()
        )
    
    def test_toy_coin_creation(self):
        toy_coin = ToyCoin.objects.get(id=self.toy_coin.id)
        self.assertEqual(toy_coin.user, self.user)
        self.assertEqual(toy_coin.name, "TOY COIN")
        self.assertEqual(toy_coin.quantity_mined, 100.00)

    def test_custom_save(self):
        # Test the enforced datetime logic in the save method
        toy_coin = ToyCoin.objects.get(id=self.toy_coin.id)
        expected_datetime = timezone.now().replace(
            month=8, 
            day=1,
            hour=0,
            minute=0,
            second=0,
            microsecond=0
        )
        self.assertEqual(toy_coin.launch_date, expected_datetime)
        
    def test_user_id_method(self):
        # Test the user_id method
        self.assertEqual(self.toy_coin.user_id, self.user.id)

# Please note that the above code assumes your Django project is set up correctly
# and that you have already run migrations for your ToyCoin and TelegramUser models.
