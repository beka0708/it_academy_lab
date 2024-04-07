serializers.py
from django.contrib.auth.models import AbstractUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password', 'is_active', 'is_superuser', 'last_login')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user