# Generated by Django 3.2.13 on 2022-05-13 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiretubers', '0008_hiretuber_tuber_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiretuber',
            name='details',
            field=models.TextField(),
        ),
    ]
