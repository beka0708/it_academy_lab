from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, SocialLinks
from django_rest_passwordreset.models import ResetPasswordToken

class SocialLinksInline(admin.StackedInline):
    model = SocialLinks
    can_delete = False
    verbose_name_plural = 'Социальные ссылки'


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('full_name', 'email', 'position', 'role')
    list_filter = ('position', 'role')
    search_fields = ('email', 'full_name', 'position')
    ordering = ('full_name',)
    filter_horizontal = ()
    inlines = [SocialLinksInline]

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Персональная информация', {'fields': ('full_name', 'image', 'about_me', 'position', 'role')}),
        ('Разрешения', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Даты', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )



admin.site.unregister(ResetPasswordToken)

admin.site.unregister(CustomUser)

admin.site.register(CustomUser, CustomUserAdmin)




