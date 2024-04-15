from django.db.models import QuerySet
from rest_framework import serializers

from form.models import Review, Client, Student


class ReviewCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Review
        exclude = ('created_at', 'updated_at')


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ('updated_at',)


class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ('status',)


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ('status',)
