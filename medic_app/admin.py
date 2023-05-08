from django.contrib import admin
from .models import Ailments, Appointment
# Register your models here.
admin.site.register([Ailments, Appointment])
