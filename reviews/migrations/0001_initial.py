# Generated by Django 4.2 on 2023-06-07 23:53

from django.db import migrations, models
import reviews.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('treated_on', models.CharField(blank=True, max_length=50, null=True)),
                ('profile_image', models.ImageField(blank=True, default=reviews.models.get_default_profile_image, max_length=255, null=True, upload_to=reviews.models.get_profile_image_filepath)),
                ('comments', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
