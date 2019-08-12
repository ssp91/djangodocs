from django.shortcuts import render

# Create your views here.
from rest_framework import generics, filters
from datamodels.serializers import UserSeializer
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend

class UserListView(generics.ListCreateAPIView):
    '''
    User list and create api.
    '''
    serializer_class = UserSeializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_fields = ['username', 'is_active']
    search_fields = ['username']


class UserActios(generics.RetrieveUpdateDestroyAPIView):
    '''
    User Retrieve Update Destroy
    '''
    serializer_class = UserSeializer
    queryset = User.objects.all()
    
