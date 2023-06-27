from django.contrib import admin

from user_interface.models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("name",)
