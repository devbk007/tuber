# Generated by Django 3.2.13 on 2022-05-05 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='redirection_url',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
    ]
