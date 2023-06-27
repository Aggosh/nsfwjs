from django.db import models

from .image_model import Image
from .property_model import Property


class ImageProperty(models.Model):
    image = models.ForeignKey(Image, blank=False, null=False, name="image", on_delete=models.CASCADE)
    property = models.ForeignKey(Property, blank=False, null=False, name="property", on_delete=models.CASCADE)
    percent = models.FloatField(blank=False, null=False, name="percent")

    def __str__(self):
        return f"{self.image.file.name} {self.property.name} {self.percent}"
