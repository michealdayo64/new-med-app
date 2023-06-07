from django.db import models

# Create your models here.


class Review(models.Model):
    name = models.CharField(max_width = 50, null = True, blank = True)
    treated 
