# Generated by Django 3.2.13 on 2022-05-06 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0004_team_more_info_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='gender',
            field=models.CharField(default='M', max_length=1),
        ),
    ]
