import asyncio
from asgiref.sync import async_to_sync

from datetime import datetime, timedelta

from aiogram import Bot
from django.db.models import F
from django.conf import settings
from celery import shared_task

from tasks.models import Task


@shared_task()
def notify_user():
    now = datetime.now()
    tasks_for_notify = Task.objects.filter(
        status=Task.TaskStatus.ACTIVE,
        deadline__range=(now, F("deadline") + timedelta(minutes=10)),
    )
    if tasks_for_notify:
        tasks = [(task.telegram_user.telegram_id, task.id) for task in tasks_for_notify]

        async def _send(tasks: list[tuple[str, str]]):
            bot = Bot(settings.BOT_TOKEN)

            tasks = []
            for telegram_id, task_id in tasks:
                tasks.append(
                    bot.send_message(telegram_id, f"Задача №{task_id} скоро истечёт!")
                )

            await asyncio.gather(*tasks)

        async_to_sync(_send)(tasks)
