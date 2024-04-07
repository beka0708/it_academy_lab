views.py
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import CustomUser

from drf_yasg.inspectors import SwaggerAutoSchema

class RegisterView(APIView):
    schema = SwaggerAutoSchema()

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token_generator = PasswordResetTokenGenerator()
            token = token_generator.make_token(user)
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = f'Click the link to activate your account: {current_site.domain}/activate/{token}/'
            send_mail(mail_subject, message, 'noreply@yourdomain.com', [user.email])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def activate_account(request, token):
    user = get_object_or_404(CustomUser, email_confirmation_token=token)
    if user.is_active:
        return HttpResponse('Account already activated.')
    user.is_active = True
    user.email_confirmation_token = None
    user.save()
    return HttpResponse('Account activated successfully.')