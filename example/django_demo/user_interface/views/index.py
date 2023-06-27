from io import BytesIO
from PIL import Image

from django.views import View
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.files import File
from django.utils import timezone

from user_interface.forms import ImageForm
from user_interface.models import Image as ImageModel
from user_interface.managers import convert_image_format, ImageScoreManager


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {"form": ImageForm()}
        return render(request, "index.html", context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        user_image = Image.open(request.FILES["image"])
        new_image = convert_image_format(user_image, "JPEG")
        blob = BytesIO()
        new_image.save(blob, "JPEG")
        image_model = ImageModel.objects.create()
        image_model.file.save(f"{timezone.now()}.jpg", File(blob))

        image_score_manager = ImageScoreManager()
        raw_image_proparties = image_score_manager.score_image(image_model.file)
        image_proparties = image_score_manager._save_scores(
            raw_image_proparties, image_model
        )

        context = {
            "image": image_model,
            "proparties": image_proparties,
            "form": ImageForm(),
        }

        return render(request, "index.html", context=context)
