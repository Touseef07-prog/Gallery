# Generated by Django 3.2.8 on 2021-10-24 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0002_picture_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]