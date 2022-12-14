# Generated by Django 3.2.13 on 2022-05-06 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0002_auto_20220506_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='camera',
            field=models.CharField(choices=[('canon', 'canon'), ('nikon', 'nikon'), ('red', 'red'), ('fuji', 'fuji'), ('panasonic', 'panasonic'), ('other', 'other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('lifestyle', 'lifestyle'), ('family', 'family'), ('travel', 'travel'), ('sports', 'sports'), ('mobile_review', 'mobile_review'), ('movie_review', 'movie_review'), ('cooking', 'cooking'), ('gaming', 'gaming')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('solo', 'solo'), ('small', 'small'), ('large', 'large')], max_length=255),
        ),
    ]
