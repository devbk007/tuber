# Generated by Django 3.2.13 on 2022-05-09 13:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('fb_link', models.URLField(blank=True)),
                ('insta_link', models.URLField(blank=True)),
                ('twitter_link', models.URLField(blank=True)),
                ('youtube_link', models.URLField(blank=True)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('edited_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
