# Generated by Django 4.2 on 2023-05-16 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medic_app', '0004_writeus'),
    ]

    operations = [
        migrations.AddField(
            model_name='writeus',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='writeus',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]