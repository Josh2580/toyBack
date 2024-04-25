from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.utils import timezone
from myTelegramUser.models import TelegramUser
from toycoin.models import ToyCoin

class ToyCoinViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.telegram_user = TelegramUser.objects.create(
            username="testuser",
            telegram_id="1234567890",
            language_code="en",
            currency="ADA"
        )
        self.list_url = reverse('toycoin-list')  # Make sure 'toycoin-list' is the correct name; adjust as needed

    def test_post_request_with_valid_data(self):
        data = {
            'name': "Super ToyCoin",
            'quantity_mined': 100,
            'time_clicked': timezone.now().isoformat(),
            'telegram_id': self.telegram_user.telegram_id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ToyCoin.objects.count(), 1)
        self.assertEqual(ToyCoin.objects.first().name, "Super ToyCoin")

    def test_get_request_returns_toycoins(self):
        ToyCoin.objects.create(
            name="Test Coin",
            quantity_mined=100,
            time_clicked=timezone.now(),
            user=self.telegram_user
        )
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # This line might need adjustment based on pagination settings

    def test_post_request_with_invalid_telegram_id(self):
        data = {
            'name': "Failed Coin",
            'quantity_mined': 100,
            'time_clicked': timezone.now().isoformat(),
            'telegram_id': "invalid12345"
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


