from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from account.models import SocialLinks

User = get_user_model()


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'image', 'full_name', 'position')


class SocialLinkSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = SocialLinks
        fields = '__all__'


class SocialUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        exclude = ('id', 'user')


class UserStudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('image', 'full_name', 'about_me', 'position',)


class UserClientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('image', 'full_name', 'about_me', 'company',)


class UserDetailSerializer(serializers.ModelSerializer):
    social = SocialUserDetailSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('full_name', 'image', 'about_me', 'position', 'social')


class UserDeveloperList(serializers.ModelSerializer):
    social = SocialUserDetailSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('full_name', 'image', 'position', 'social')



class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    password2 = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        password2 = attrs.pop('password2')
        if attrs['password'] != password2:
            raise serializers.ValidationError("Passwords don't match!")
        validate_password(attrs['password'])
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user



