from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source="get_status_display", read_only=True)
    telegram_user_id = serializers.IntegerField(source="telegram_user.id")

    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "deadline",
            "description",
            "status",
            "telegram_user_id",
        )


class TaskUpdateSerializer(serializers.ModelSerializer):
    deadline = serializers.DateTimeField(read_only=True)
    title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    status = serializers.ChoiceField(
        source="get_status_display", choices=Task.TaskStatus.choices
    )
    telegram_user_id = serializers.IntegerField(
        source="telegram_user.id", read_only=True
    )

    class Meta:
        model = Task
        fields = (
            "id",
            "status",
            "deadline",
            "title",
            "description",
            "telegram_user_id",
        )
