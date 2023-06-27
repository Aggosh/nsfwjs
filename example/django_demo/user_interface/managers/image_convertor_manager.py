from io import BytesIO
from PIL import Image


def convert_image_format(img_obj: Image, output_format: str = None) -> Image:
    """Convert image format."""

    new_img_obj = img_obj
    if output_format and (img_obj.format != output_format):
        image_bytes_IO = BytesIO()
        img_obj = img_obj.convert('RGB')
        img_obj.save(image_bytes_IO, output_format)
        new_img_obj = Image.open(image_bytes_IO)

    return new_img_obj
