# Generated by Django 3.2.13 on 2022-05-09 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0011_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='title',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]