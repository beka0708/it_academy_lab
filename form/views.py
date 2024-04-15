from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from rest_framework import mixins, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from account.send_mail import send_confirmation_email
from account.utils import generate_unique_password
from form.models import Review, Client, Student
from form.serializers import ReviewCreateSerializer, ClientCreateSerializer, StudentCreateSerializer, \
    ReviewListSerializer


User = get_user_model()

class ReviewCreateListView(mixins.CreateModelMixin,mixins.ListModelMixin, GenericViewSet):

    #Получаю отзывы только те в которых больше 3 звезд, ну и + если пользователь \
    # оставил плохой отзыв то он показывается только ему
    def get_queryset(self):
        if self.action == 'list':
            user = self.request.user
            reviews = Review.objects.filter(rating__gte=4)
            if user.is_authenticated:
                reviews |= Review.objects.filter(user=user)
            return reviews
        return Review.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        return [AllowAny()]

    def get_serializer_class(self):
        if self.action == 'create':
            return ReviewCreateSerializer
        return ReviewListSerializer

    def create(self, request, *args, **kwargs):
        if Review.objects.filter(user=request.user).exists():
            return Response('Review already exists', status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ClientCreateView(mixins.CreateModelMixin, GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientCreateSerializer
    permission_classes = [AllowAny]





class StudentCreateView(mixins.CreateModelMixin, GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer
    permission_classes = [AllowAny]