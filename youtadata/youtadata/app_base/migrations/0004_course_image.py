# Generated by Django 2.2.4 on 2019-08-08 06:07

import app_base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_base', '0003_auto_20190806_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(null=True, upload_to=app_base.models.course_image_path),
        ),
    ]
