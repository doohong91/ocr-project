# Generated by Django 3.1 on 2020-09-02 04:42

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_img', models.ImageField(upload_to=api.models.user_directory_path)),
                ('result_img', models.ImageField(upload_to=api.models.user_directory_path)),
                ('bounding_boxes', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
