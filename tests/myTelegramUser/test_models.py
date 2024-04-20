from django.test import TestCase
from myTelegramUser.models import TelegramUser


class TelegramUserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Creating a user for use in all tests
        cls.user1 = TelegramUser.objects.create(
            username="user1", 
            first_name="John", 
            last_name="Doe", 
            full_name="John Doe", 
            telegram_id="123456789", 
            language_code="en", 
            currency="ADA"
        )
        
    def test_telegram_user_creation(self):
        user = TelegramUser.objects.get(telegram_id="123456789")
        self.assertEqual(user.username, "user1")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.currency, "ADA")
        
    def test_telegram_user_string_representation(self):
        user = TelegramUser.objects.get(telegram_id="123456789")
        self.assertEqual(str(user), "123456789")


