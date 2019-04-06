from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Doctor
from .serializers import DoctorSerializer, UserSerializer, CurrentUserSerializer, AppointmentSerializer
from django.shortcuts import render
from django.contrib.auth.models import User

@api_view(['GET'])
def get_doctors(request):
    
    if request.method == 'GET':
        docs = Doctor.objects.all()
        serializer = DoctorSerializer(docs, many=True)
        return Response(serializer.data)
    return Response({})

@api_view(['GET'])
def get_doctor(request, pk):
    try:
        doc = Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DoctorSerializer(doc)
        return Response(serializer.data)
    
    return Response({})   

@api_view(['GET'])
def get_user(request, pk):
    try:
        doc = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(doc)

        if request.user == doc:
            return Response(serializer.data)
    
    return Response({})    

@api_view(['GET'])
def get_current_user(request):
    user = CurrentUserSerializer(request.user)    
    return Response(user.data) 

def home(request):
    return render(request, 'frontend/index.html')



@api_view(['POST'])
def create_appointment(request):
    data = {
        'time':  request.data.get('time'),
        'date':  request.data.get('date'),
        'duration':  request.data.get('duration'),
        'doctor':  Doctor.objects.get(pk=request.data.get('doctor')), 
        'patient': request.user,
    }

    serializer = AppointmentSerializer(data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
