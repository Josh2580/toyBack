from django.contrib import admin
from .models import ToyCoin


class ToyCoinAdmin(admin.ModelAdmin):
    list_display = ("user", "user_id", "get_total_users", "quantity_mined",  "get_total_quantity_mined" )


admin.site.register(ToyCoin, ToyCoinAdmin)
# admin.site.register(ToyCoin)
