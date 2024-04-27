from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from project.models import Project, Developer
from project.serializers import ProjectListSerializer, ProjectDetailSerializer, DeveloperListSerializer, \
    DeveloperDetailSerializer


class ProjectListDetailView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Project.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectListSerializer
        return ProjectDetailSerializer


class DeveloperListDetailView(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Developer.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == "list":
            return DeveloperListSerializer
        return DeveloperDetailSerializer



