from rest_framework import serializers
from django.contrib.auth.models import User

class UserSeializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = '__all__'