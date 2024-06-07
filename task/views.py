from rest_framework import viewsets, permissions, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .models import Task
from .serializers import TaskSerializer
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


