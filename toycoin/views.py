from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework import status
from rest_framework.response import Response
from toycoin.models import ToyCoin
from toycoin.serializers import ToyCoinSerializer, CreateToyCoinSerializer
from myTelegramUser.models import TelegramUser
from django.http import  JsonResponse
# Create your views here.


class ToyCoinViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ToyCoin.objects.all()
    serializer_class = ToyCoinSerializer
    lookup_field = 'user__telegram_id'

    def perform_create(self, serializer):
        telegram_id = self.request.data.get('telegram_id')

        if not telegram_id:
            return Response({"error": "Telegram ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            telegram_user = TelegramUser.objects.get(telegram_id=telegram_id)
        except TelegramUser.DoesNotExist:
            return Response({"error": "TelegramUser not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer.save(user=telegram_user)
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateToyCoinSerializer
        return ToyCoinSerializer
    
    