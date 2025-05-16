from django.db import models


class Task(models.Model):
    class TaskStatus(models.TextChoices):
        ACTIVE = "active", "Active"
        DONE = "done", "Done"
        EXPIRED = "expired", "expired"

    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    telegram_user = models.ForeignKey("TelegramUser", on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20, choices=TaskStatus.choices, default=TaskStatus.ACTIVE
    )

    class Meta:
        db_table = "tasks"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class TelegramUser(models.Model):
    telegram_id = models.CharField(max_length=20)

    class Meta:
        db_table = "telegram_users"
        verbose_name = "Пользователь телеграм"
        verbose_name_plural = "Пользователи телеграм"
