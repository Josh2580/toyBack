from rest_framework import viewsets, permissions, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer
from myTelegramUser.models import TelegramUser

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # lookup_field = 'user__telegram_id'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user__telegram_id']

    def partial_update(self, request, *args, **kwargs):
        task = self.get_object()
        telegram_id = request.data.get('telegram_id')
        user = TelegramUser.objects.get(telegram_id=telegram_id)  # Ensure this user exists and is fetched correctly
        if user:  
            task.user.add(user)  # Adding a user to the Many-to-Many relationship
        task.save()
        return Response(self.get_serializer(task).data, status=status.HTTP_200_OK)