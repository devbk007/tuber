# Generated by Django 3.2.13 on 2022-05-12 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0006_youtuber_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='email',
            field=models.CharField(max_length=255),
        ),
    ]
