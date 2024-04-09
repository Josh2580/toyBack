from django.shortcuts import render
from rest_framework import permissions, viewsets
from toycoin.models import ToyCoin
from toycoin.serializers import ToyCoinSerializer
# Create your views here.


class ToyCoinViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ToyCoin.objects.all()
    serializer_class = ToyCoinSerializer
    lookup_field = 'user__telegram_id'
