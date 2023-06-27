import json
import os

import requests

from PIL import Image

from user_interface.models import Property, ImageProperty, Image as ImageModel


class ImageScoreManager:
    def score_image(self, image: Image) -> list:
        url = f"{os.environ['NODE_SERVER_URL']}:8080/nsfw"
        file_image = {"image": image}

        res = requests.post(url, files=file_image)

        return json.loads(res.text)

    def _save_scores(self, response: list, image_model: ImageModel) -> list:
        image_properties = []

        for property in response:
            name = property.get("className")
            percent = property.get("probability")
            if name and percent:
                property, _ = Property.objects.get_or_create(name=name)
                image_properties.append(ImageProperty.objects.create(
                    image=image_model, property=property, percent=float(percent)
                ))

        return image_properties
