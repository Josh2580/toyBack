# from django.test import TestCase
# from rest_framework.exceptions import ValidationError
# from myTelegramUser.serializers import TelegramUserSerializer
# from myTelegramUser.models import TelegramUser

# class TelegramUserSerializerTestCase(TestCase):
#     def setUp(self):
#         # Create a TelegramUser instance to use in tests
#         self.user = TelegramUser.objects.create(
#             username="user123",
#             telegram_id="123456789",
#             language_code="en",
#             currency="USD"
#         )

#         # Assuming you have a field like 'referrer' that could be another TelegramUser
#         self.referrer_user = TelegramUser.objects.create(
#             username="referrerUser",
#             telegram_id="987654321",
#             language_code="en",
#             currency="EUR"
#         )
#         self.user.referrer = self.referrer_user
#         self.user.save()

#     def test_serialization(self):
#         # Serialize the user
#         serializer = TelegramUserSerializer(self.user)
#         # Check that all fields are included
#         data = serializer.data
#         self.assertEqual(set(data.keys()), set(['id', 'username', 'last_name','full_name','first_name', 'telegram_id', 'language_code', 'currency', 'referrer', 'user_coin', 'referred_users']))
#         self.assertEqual(data['username'], 'user123')
#         # print(f"printing {data['referrer']['telegram_id']}")
#         # self.assertEqual(data['referrer'], str(self.referrer_user))  # Ensure this uses the string representation

#     def test_deserialization(self):
#         # Create data for creating a new user
#         data = {
#             'username': 'newuser',
#             'telegram_id': '1122334455',
#             'language_code': 'fr',
#             'currency': 'EUR'
#         }
#         serializer = TelegramUserSerializer(data=data)
#         # Validate data
#         if serializer.is_valid():
#             new_user = serializer.save()
#             self.assertEqual(new_user.username, 'newuser')
#         else:
#             self.fail(serializer.errors)

#     def test_invalid_data(self):
#         # Try to create a user with incomplete data
#         data = {
#             'username': '',
#             'telegram_id': '1122334455'
#         }
#         # serializer = TelegramUserSerializer(data=data)
#         # self.assertFalse(serializer.is_valid())
#         # self.assertIn('username', serializer.errors)  # Assuming username is required

