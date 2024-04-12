from django.db import models

from django.db import models


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/', verbose_name="Изображение")

    def __str__(self):
        return f'{self.image}'

    class Meta:
        verbose_name = "Галлерея"
        verbose_name_plural = verbose_name


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    short_body = models.TextField(max_length=500, verbose_name="краткое описание")
    body = models.TextField(verbose_name='Содержимое')
    speaker = models.CharField(max_length=255, verbose_name="Спикер")
    preview = models.ForeignKey(Gallery, verbose_name="Превью", related_name='news', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class NewsImage(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='news/')
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f"Image {self.title}"


    class Meta:
        verbose_name = "Изображение новости"
        verbose_name_plural = "Изображения новостей"


class AboutUs(models.Model):
    body = models.TextField(max_length=5000, verbose_name="Текст")

    def __str__(self):
        return f'{self.body[:50]}...'

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"


class AboutUsImages(models.Model):
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='about_us/', verbose_name="Изображение")

    def __str__(self):
        return f"Images about us"

