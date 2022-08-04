
from rest_framework import serializers
from .models import Tour
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ('id', 'name', 'description')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_Kwargs = {'password': {'write_only': True, 'require': True}}

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        token = Token.objects.create(user=user)
        return user











