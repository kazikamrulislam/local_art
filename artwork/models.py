from django.db import models
from datetime import datetime
from django.conf import settings
from django.db import models

# Create your models here.


class Artwork(models.Model):
    art_title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.art_title}, {self.artist}, {self.photo_main}, {self.list_date}"