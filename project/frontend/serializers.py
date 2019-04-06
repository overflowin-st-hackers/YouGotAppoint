from rest_framework import serializers
from .models import Doctor, Specialization

class DoctorSerializer(serializers.ModelSerializer):
    specializations = serializers.StringRelatedField(many=True);

    class Meta:
        model = Doctor
        fields = ('name', 'rating', 'degrees', 'contact_no', 'specializations', 'pk')