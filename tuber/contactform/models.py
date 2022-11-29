from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime

# Create your models here.

class Contactform(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    company_name = models.CharField(max_length=255, blank=True)
    subject = models.CharField(max_length=255)
    details = RichTextField(max_length=255)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.full_name