from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from myTelegramUser.models import TelegramUser
from toycoin.models import ToyCoin
from django.utils import timezone

class ToyCoinViewSetTest(APITestCase):

    def setUp(self):
        # Create a TelegramUser
        self.telegram_user = TelegramUser.objects.create(
            username="testuser",
            telegram_id="1234567890",
            language_code="en",
            currency="ADA"
        )
        # URL for creating ToyCoins
        self.create_url = reverse('toycoin-list')  # Update 'toycoin-list' with the actual name used in your urls.py

    def test_create_toycoin_with_valid_data(self):
        """
        Ensure we can create a new ToyCoin with valid telegram_id.
        """
        data = {
            'name': "Super ToyCoin",
            'quantity_mined': 100,
            'time_clicked': timezone.now(),
            'telegram_id': self.telegram_user.telegram_id
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ToyCoin.objects.count(), 1)
        self.assertEqual(ToyCoin.objects.get().name, "Super ToyCoin")

    def test_create_toycoin_with_invalid_telegram_id(self):
        """
        Ensure we get a 404 when trying to create a ToyCoin with a non-existent telegram_id.
        """
        data = {
            'name': "Super ToyCoin",
            'quantity_mined': 100,
            'time_clicked': timezone.now(),
            'telegram_id': "nonexistent123"
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_toycoin_without_telegram_id(self):
        """
        Ensure we get a 400 error when telegram_id is not provided.
        """
        data = {
            'name': "Super ToyCoin",
            'quantity_mined': 100,
            'time_clicked': timezone.now(),
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_toycoin_list(self):
        """
        Ensure we can retrieve a list of ToyCoins.
        """
        ToyCoin.objects.create(name="ToyCoin 1", quantity_mined=50, time_clicked=timezone.now(), user=self.telegram_user)
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Adjust according to pagination if applied
