from typing import Any
from django.db import models

# Create your models here.
class ImageUpload(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return (
            f'Image upload at {self.uploaded_at}'
        )