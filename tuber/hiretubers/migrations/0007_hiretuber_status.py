# Generated by Django 3.2.13 on 2022-05-12 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiretubers', '0006_auto_20220512_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiretuber',
            name='status',
            field=models.CharField(default='Screening', max_length=255),
        ),
    ]