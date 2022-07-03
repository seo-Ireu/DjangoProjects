from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
class Picture(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="img")
    objects = models.Manager()
    image_thumbnail=ImageSpecField(source='image',processors=[ResizeToFill(80,80)])

    def __str__(self):
        return self.text


