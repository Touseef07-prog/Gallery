# Generated by Django 3.2.8 on 2021-10-24 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]