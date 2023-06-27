from django.contrib import admin
from django.utils.html import format_html

from user_interface.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("created_at", "file", "image_tag")
    readonly_fields = ("image_tag",)

    def image_tag(self, obj):
        return format_html(
            f'<img src="{obj.file.url}" style="max-width:200px; max-height:200px; float:right;"/>'
        )

    image_tag.allow_tags = True
