from distutils.command.upload import upload
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save, post_init
from django.core.mail import send_mail
from tuber.settings import EMAIL_HOST_USER

# Create your models here.

CAMERA = [
    ('canon', 'canon'),
    ('nikon', 'nikon'),
    ('red', 'red'),
    ('fuji', 'fuji'),
    ('panasonic', 'panasonic'),
    ('other', 'other'),
]

CREW = [
    ('solo', 'solo'),
    ("small","small"),
    ('large', 'large'),
]

CATEGORY = [
    ('lifestyle', 'lifestyle'),
    ('family', 'family'),
    ('travel', 'travel'),
    ('sports', 'sports'),
    ('mobile_review', 'mobile_review'),
    ('movie_review', 'movie_review'),
    ('cooking', 'cooking'),
    ('gaming', 'gaming'),
]

STATUS = [
    ('active', 'active'),
    ('inactive', 'inactive'),
    ('suspended', 'suspended'),
    ('hold', 'hold'),
]

class Youtuber(models.Model):
    status = models.CharField(max_length=255, default='active', choices=STATUS)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media/youtubers/%Y/%m/')
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    city = models.CharField(max_length=255)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(max_length=255, choices=CREW)
    camera = models.CharField(max_length=10, choices=CAMERA)
    subs_count = models.IntegerField()
    category = models.CharField(max_length=255, choices=CATEGORY)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    previous_status = None

    def __str__(self):
        return self.first_name

#     @staticmethod
#     def post_save(sender, instance, created, **kwargs):
#         if instance.previous_status != instance.status or created:
#             # Sending welcome mail
#             subject = 'Status Change Notifier'
#             message = 'Hi ytuber, your collaboration status has been changed to : ' + str(instance.status)
#             recepient = str(instance.email)
#             send_mail(subject, 
#                 message, EMAIL_HOST_USER, [recepient], fail_silently = False)
            

#     @staticmethod
#     def remember_status(sender, instance, **kwargs):
#         instance.previous_status = instance.status

# post_save.connect(Youtuber.post_save, sender=Youtuber)
# post_init.connect(Youtuber.remember_status, sender=Youtuber)