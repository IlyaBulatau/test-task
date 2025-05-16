from datetime import datetime, timedelta

from django.db.models import F
from celery import shared_task
from tasks.models import Task


@shared_task
def notify_user():
    now = datetime.now()
    tasks_for_notify = Task.objects.filter(
        status=Task.TaskStatus.ACTIVE,
        deadline__range=(now, F("deadline") + timedelta(minutes=10)),
    )

    for task in tasks_for_notify:
        ...
        # TODO
