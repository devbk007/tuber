# Generated by Django 3.2.13 on 2022-05-09 15:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactinfo', '0002_alter_contactinfo_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='address',
            field=ckeditor.fields.RichTextField(default=0),
            preserve_default=False,
        ),
    ]
