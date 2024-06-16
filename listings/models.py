from django.db import models
from django.db.models import Model, CharField, IntegerField, DecimalField, TextField, FileField, BooleanField, DateTimeField

def image_path(instance, filename):
    return f"listings/images/{instance.id}/{filename}"


class Listing(models.Model):
    title = models.CharField(max_length=200)
    location = models.TextField(max_length=128)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    rooms = models.IntegerField()
    sqft = models.IntegerField()
    photo_main = models.FileField(upload_to=image_path)
    is_published = models.BooleanField(default=True)
    is_booked = models.BooleanField(default=False)
    posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title