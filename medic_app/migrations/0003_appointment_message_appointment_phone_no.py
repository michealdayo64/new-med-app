# Generated by Django 4.2 on 2023-05-14 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medic_app', '0002_remove_appointment_time_from_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='phone_no',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
