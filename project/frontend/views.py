from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Doctor
from .serializers import DoctorSerializer, UserSerializer, CurrentUserSerializer
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

        if request.user == doc
        return Response(serializer.data)
    
    return Response({})    

@api_view(['GET'])
def get_current_user(request):
    user = CurrentUserSerializer(request.user)    
    return Response(user.data) 

def home(request):
    return render(request, 'frontend/index.html')