from rest_framework import viewsets, permissions

from .models import TelegramUser
from .serializers import TelegramUserSerializer

class TelegramUserViewSet(viewsets.ModelViewSet):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer
    lookup_field = 'telegram_id'