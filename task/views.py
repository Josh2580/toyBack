from rest_framework import viewsets, permissions, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .models import Task, AutoBot
from .serializers import TaskSerializer, AutoBotSerializer
from myTelegramUser.models import TelegramUser



class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user__telegram_id']
    lookup_field = 'group_id'

    def partial_update(self, request, *args, **kwargs):
        task = self.get_object()
        telegram_id = request.data.get('telegram_id', None)  # Default to None if not provided

        if telegram_id:
            try:
                user = TelegramUser.objects.get(telegram_id=telegram_id)
                task.user.add(user)  # Adding a user to the Many-to-Many relationship
                task.save()
            except TelegramUser.DoesNotExist:
                raise NotFound(detail="User with the given telegram_id does not exist")

        serializer = self.get_serializer(task, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)


class AutoBotViewSet(viewsets.ModelViewSet):
    queryset = AutoBot.objects.all()
    serializer_class = AutoBotSerializer
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