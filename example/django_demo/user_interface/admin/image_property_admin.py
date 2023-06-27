from django.contrib import admin

from user_interface.models import ImageProperty


@admin.register(ImageProperty)
class ImagePropertyAdmin(admin.ModelAdmin):
    list_display = ("image", "property", "percent")
    list_filter = ("property",)
