# Generated by Django 3.2.13 on 2022-05-10 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0013_chooseus_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chooseus',
            name='happy_customers',
            field=models.CharField(max_length=255),
        ),
    ]