from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/doctors/',views.get_doctors,name='get_doctors'),
    path('api/doctors/<int:pk>/',views.get_doctor,name='get_doctor'),
    path('api/users/',views.get_users,name='get_users'),
    path('api/users/<int:pk>/',views.get_user,name='get_user'),
]