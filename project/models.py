from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Developer(models.Model):
    developer = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Разработчик")

    def __str__(self):
        return self.developer.email

    class Meta:
        verbose_name = "Разработчик"
        verbose_name_plural = "Разработчики"


class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    preview = models.ImageField(upload_to='preview_projects/', verbose_name="Изображение", blank=True, null=True)
    link_to_project = models.URLField(verbose_name="Ссылка")
    developers = models.ManyToManyField(Developer, related_name='projects', verbose_name="Разработчики")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class ProjectSImage(models.Model):
    image = models.ImageField(upload_to='project_images/', verbose_name="Изображение проекта")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = "Изображение проекта"
        verbose_name_plural = "Изображения проектов"

