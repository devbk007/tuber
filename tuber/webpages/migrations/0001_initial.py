# Generated by Django 3.2.13 on 2022-05-05 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('button_text', models.CharField(default='Read More', max_length=255)),
                ('photo', models.ImageField(upload_to='media/slider/%Y/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]