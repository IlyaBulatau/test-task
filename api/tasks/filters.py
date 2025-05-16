from django_filters import rest_framework as filters

from tasks.models import Task


class TaskFilterSet(filters.FilterSet):
    telegram_user_id = filters.CharFilter(field_name="telegram_user__id")

    class Meta:
        model = Task
        fields = ("telegram_user_id",)
