from unittest.util import _MAX_LENGTH
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

GENDER = [
    ('m', 'Male'),
    ('f', 'Female'),
    ('t', 'Transgender'),
]

class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255, default="Read More")
    redirection_url = models.URLField()
    photo = models.ImageField(upload_to='media/slider/%Y/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER)
    yt_link = models.URLField()
    fb_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    photo = models.ImageField(upload_to='media/team/%Y/%m/%d/')
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

class About(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/about/%Y/%m/')
    description = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Services(models.Model):
    service_type = models.CharField(max_length=255)
    fees = models.CharField(max_length=255)
    yt_link = models.URLField()
    photo = models.ImageField(upload_to = 'media/services/%Y/%m/')
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.service_type

class Chooseus(models.Model):
    year_experience = models.IntegerField()
    happy_customers = models.CharField(max_length=255)
    completed_projects = models.IntegerField()
    happy_creators = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    description = models.TextField()
    yt_link = models.URLField()

    def __str__(self):
        return self.happy_customers
