# Generated by Django 3.2.13 on 2022-05-13 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiretubers', '0009_alter_hiretuber_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiretuber',
            name='status',
            field=models.CharField(choices=[('Screening', 'Screening'), ('Accept', 'Accept'), ('Hold', 'Hold'), ('Reject', 'Reject')], default='Screening', max_length=255),
        ),
    ]