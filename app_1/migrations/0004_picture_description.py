# Generated by Django 3.2.8 on 2021-10-24 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0003_category_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='description',
            field=models.TextField(max_length=60, null=True),
        ),
    ]
