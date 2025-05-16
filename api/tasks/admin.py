from django.contrib import admin

from tasks.models import Task, TelegramUser


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    pass
