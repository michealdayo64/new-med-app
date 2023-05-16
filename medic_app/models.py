from django.db import models
from auths.models import Account
# Create your models here.

class WriteUs(models.Model):
    firstname = models.CharField(max_length = 50, null = True, blank = True)
    lastname = models.CharField(max_length = 50, null = True, blank = True)
    email = models.EmailField(null = True, blank=True)
    phone_no = models.CharField(max_length = 50, null = True, blank = True)
    message = models.TextField(null = True, blank = True)

    def __str__(self):
        return email


class Ailments(models.Model):
    user = models.ForeignKey(Account, default=False, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length = 100, null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    image_icon = models.ImageField(upload_to = 'picture', null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

class Appointment(models.Model):
    user = models.ForeignKey(Account, default=False, on_delete=models.CASCADE, null=True, blank=True)
    ailment_id = models.ForeignKey(Ailments, null = True, blank = True, on_delete = models.CASCADE)
    phone_no = models.CharField(max_length=30, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    date = models.DateField()
    appointment_time = models.CharField(max_length=20, null=True, blank=True)


    def __str__(self):
        return f'{self.user}'
