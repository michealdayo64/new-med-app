# Generated by Django 4.2 on 2023-06-06 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0003_additionalinformation_my_insure_carrier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additionalinformation',
            name='user',
        ),
        migrations.AddField(
            model_name='additionalinformation',
            name='email',
            field=models.EmailField(blank=True, max_length=60, null=True, unique=True, verbose_name='email'),
        ),
        migrations.AddField(
            model_name='additionalinformation',
            name='fifteen_min_trial',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='additionalinformation',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='additionalinformation',
            name='lastname_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='additionalinformation',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]