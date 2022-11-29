from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime

# Create your models here.

class Contactinfo(models.Model):
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    fb_link = models.URLField(blank=True)
    insta_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    youtube_link = models.URLField(blank=True)
    address = RichTextField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone
