# Generated by Django 3.2.13 on 2022-05-09 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactform', '0002_alter_contactform_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='phone',
            field=models.CharField(max_length=255),
        ),
    ]
