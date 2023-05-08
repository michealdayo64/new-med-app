from django.db import models

# Create your models here.

class Ailments(models.Model):
    title = models.CharField(max_length = 100, null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    image_icon = models.ImageField(upload_to = 'picture/', null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

class Appointment(models.Model):
    ailment_id = models.ForeignKey(Ailments, null = True, blank = True, on_delete = models.CASCADE)
    date = models.DateField()
    time_from = models.TimeField()
    time_to = models.TimeField()

    def __str__(self):
        return f'{self.id}'
