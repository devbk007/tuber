# Generated by Django 3.2.13 on 2022-05-10 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0017_services_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='description',
        ),
    ]
