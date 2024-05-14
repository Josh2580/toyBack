from django.contrib import admin
from .models import TelegramUser


# Register your models here.

class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ("get_online_users", "get_daily_users", "get_total_users", "last_active", "telegram_id", "full_name", "username" )


admin.site.register(TelegramUser, TelegramUserAdmin)
