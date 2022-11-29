from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
from django.db.models.signals import post_save, post_init
from django.core.mail import send_mail
from tuber.settings import EMAIL_HOST_USER
# Create your models here.

STATUS = [
    ('Screening', 'Screening'),
    ('Accept', 'Accept'),
    ('Hold', 'Hold'),
    ('Reject', 'Reject'),
]

class Hiretuber(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    tuber_name =  models.CharField(max_length=255)
    tuber_id = models.CharField(max_length=255)
    tuber_email = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default="Screening", choices=STATUS)
    details = models.TextField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    previous_status = None

    def __str__(self):
        return self.first_name

#     @staticmethod
#     def post_save(sender, instance, created, **kwargs):
#         if instance.previous_status != instance.status or created:
#             # Sending welcome mail
#             subject = 'YTuber collaboration Status Notifier'
#             message_tuber = """Hi {tuber_name},
#             Collaboration status has changed to : {status}.                 
#             Details of project : {details}""".format(tuber_name=instance.tuber_name, status = instance.status, details=instance.details)

#             message_user = """Hi {first_name},
#             Collaboration status with {tuber_name} has changed to : {status}.
#             Details of project : {details}""".format(first_name=instance.first_name, tuber_name=instance.tuber_name , status = instance.status, details=instance.details)

#             recepient1 = str(instance.email)
#             recepient2 = str(instance.tuber_email)

#             send_mail(subject, 
#                 message_tuber, EMAIL_HOST_USER, [recepient2], fail_silently = False)
            
#             send_mail(subject, 
#                 message_user, EMAIL_HOST_USER, [recepient1], fail_silently = False)

#     @staticmethod
#     def remember_status(sender, instance, **kwargs):
#         instance.previous_status = instance.status

# post_save.connect(Hiretuber.post_save, sender=Hiretuber)
# post_init.connect(Hiretuber.remember_status, sender=Hiretuber)
