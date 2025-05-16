import os
from datetime import timedelta

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.settings")

app = Celery("celery")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks(["tasks.bg_tasks"])


app.conf.beat_schedule = {
    "test": {
        "task": "tasks.bg_tasks.notify_user",
        "schedule": timedelta(seconds=10),
    },
}
