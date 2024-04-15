from django.shortcuts import render
from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from social.models import News, AboutUs
from social.serializers import NewsDetailSerializer, NewsListSerializer, AboutUsSerializer


class NewsRetrieveListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = News.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'list':
            return NewsListSerializer
        return NewsDetailSerializer


class AboutsUsViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = AboutUs.objects.all()
    permission_classes = [AllowAny]
    serializer_class = AboutUsSerializer




