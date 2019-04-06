from django.contrib import admin
from .models import Specialization, Doctor, Appointment
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Specialization)
admin.site.register(Appointment)