from django.contrib import admin
from .models import ToyCoin


class ToyCoinAdmin(admin.ModelAdmin):
    list_display = ("user", "quantity_mined" )


admin.site.register(ToyCoin, ToyCoinAdmin)
# admin.site.register(ToyCoin)
