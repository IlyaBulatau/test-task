from rest_framework import viewsets

from tasks.filters import TaskFilterSet
from tasks.models import Task, TelegramUser
from tasks.serializers import TaskSerializer, TaskUpdateSerializer


class TaskViewSet(viewsets.ModelViewSet):
    http_method_names = ("get", "post", "patch")
    queryset = Task.objects.select_related("telegram_user").all()
    filterset_class = TaskFilterSet

    def get_serializer_class(self):
        if self.action == "partial_update":
            return TaskUpdateSerializer

        return TaskSerializer

    def perform_create(self, serializer):
        telegram_user_id = serializer.validated_data.pop("telegram_user").get("id")

        user, _ = TelegramUser.objects.get_or_create(telegram_id=telegram_user_id)

        serializer.save(telegram_user_id=user.id)
