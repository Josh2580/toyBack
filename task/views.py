from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # lookup_field = 'user__telegram_id'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user__telegram_id']