from rest_framework import serializers
from account.serializers import UserDetailSerializer, UserDeveloperList
from project.models import Project, ProjectSImage, Developer


class DeveloperListSerializer(serializers.ModelSerializer):
    developer = UserDeveloperList(read_only=True)

    class Meta:
        model = Developer
        fields = ("__all__")


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'preview',)


class DeveloperDetailSerializer(serializers.ModelSerializer):
    developer = UserDetailSerializer(read_only=True)
    projects = ProjectListSerializer(many=True, read_only=True)

    class Meta:
        model = Developer
        fields = ('__all__')


# Сериализатор для детальной информации о разработчике при просмотре проекта
class DeveloperDetailForProjectSerializer(serializers.ModelSerializer):
    developer = UserDetailSerializer(read_only=True)

    class Meta:
        model = Developer
        fields = ('__all__')


class ProjectImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSImage
        fields = ('image',)


class ProjectDetailSerializer(serializers.ModelSerializer):
    images = ProjectImagesSerializer(many=True, read_only=True)
    developers = DeveloperDetailForProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        exclude = ('preview',)


