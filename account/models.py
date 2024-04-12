
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from account.managers import UserManager

BACKEND = 'backend'
FRONTEND = 'frontend'
PROJECT_MANAGER = 'project_manager'
UI_UX_DESIGNER = 'ui_ui_designer'
TESTER = 'tester'

POSITION_CHOICES = [
    (BACKEND, 'Backend'),
    (FRONTEND, 'Frontend'),
    (PROJECT_MANAGER, 'Project Manager'),
    (UI_UX_DESIGNER, 'UI UX Designer'),
    (TESTER, 'Tester')
]

class CustomUser(AbstractUser):

    ROLE_CHOICES = [
        ('client', 'Клиент'),
        ('student', 'Студент'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, blank=True, null=True, verbose_name="Тип аккаунта")
    username = models.CharField(max_length=255, unique=False, blank=True, null=True)
    email = models.EmailField(_("email address"), unique=True)
    full_name = models.CharField(max_length=128, verbose_name="ФИО")
    phone_number = PhoneNumberField('Номер телефона', help_text='Пример: +996700777777')
    position = models.CharField(max_length=20, choices=POSITION_CHOICES, verbose_name="Позиция", blank=True, null=True)
    company = models.CharField(max_length=50, choices=ROLE_CHOICES, verbose_name="Компания", blank=True, null=True)
    image = models.ImageField(upload_to='avatars/', verbose_name="Аватар", blank=True, null=True, default='avatars/default_avatar.jpg')
    about_me = models.TextField(blank=True, null=True, verbose_name="О себе")

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"


class SocialLinks(models.Model):
    user = models.OneToOneField(CustomUser, related_name='social', on_delete=models.CASCADE)
    telegram = models.URLField(max_length=512, verbose_name="Телеграм", blank=True, null=True)
    facebook = models.URLField(max_length=512, verbose_name="Фейсбук", blank=True, null=True)
    instagram = models.URLField(max_length=512, verbose_name="Инстаграмм", blank=True, null=True)
    linkedin = models.URLField(max_length=512, verbose_name="Линкдин", blank=True, null=True)
    github = models.URLField(max_length=512, verbose_name="ГитХаб", blank=True, null=True)
    site_cv = models.URLField(max_length=512, verbose_name="Персональный сайт", blank=True, null=True)
    vk = models.URLField(max_length=512, verbose_name="ВКонтакте", blank=True, null=True)

    def __str__(self):
        return f"Сoц сети {self.user}"

    class Meta:
        verbose_name = "Ссылка на соц. сеть"
        verbose_name_plural = "Ссылки на соц. сети"
