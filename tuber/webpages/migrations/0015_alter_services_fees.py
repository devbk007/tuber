# Generated by Django 3.2.13 on 2022-05-10 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0014_alter_chooseus_happy_customers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='fees',
            field=models.CharField(max_length=255),
        ),
    ]
