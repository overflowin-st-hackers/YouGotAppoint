from rest_framework import serializers
from .models import Doctor, Specialization, Appointment
from django.contrib.auth.models import User

class AppointmentSerializer1(serializers.ModelSerializer):
   
    class Meta:
        model = Appointment
        fields = ('date', 'time', 'duration', 'patient')

class AppointmentSerializer2(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ('date', 'time', 'duration', 'doctor')

class DoctorSerializer(serializers.ModelSerializer):
    specializations = serializers.StringRelatedField(many=True);
    appointments = AppointmentSerializer1(many=True)

    class Meta:
        model = Doctor
        fields = ('name', 'rating', 'degrees', 'contact_no', 'specializations', 'pk', 'appointments')


class UserSerializer(serializers.ModelSerializer):
    appointments = AppointmentSerializer2(many=True)

    class Meta:
        model = User
        fields = ('username', 'appointments')

class CurrentUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk','username')
