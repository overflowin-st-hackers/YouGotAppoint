from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0)
    degrees = models.CharField(max_length=300, null=True)
    no_of_reviews = models.IntegerField(default=0)
    contact_no = models.BigIntegerField()

    def __str__(self):
        return self.name

class Specialization(models.Model):
    disease = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, related_name='specializations', on_delete=models.CASCADE)

    def __str__(self):
        return self.disease

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='appointments', on_delete=models.CASCADE)
    patient = models.ForeignKey(User, related_name='appointments', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    duration = models.DurationField()
