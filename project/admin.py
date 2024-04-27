from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Project, ProjectSImage, Developer


User = get_user_model()


class ProjectSImageInline(admin.TabularInline):
    model = ProjectSImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'link_to_project')
    search_fields = ('title', 'description')
    inlines = [ProjectSImageInline]


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'position', 'about_me')
    search_fields = ('developer__email', 'developer__full_name')

    def email(self, obj):
        related_user = obj.developer
        return related_user.email
    email.short_description = 'Email'

    def position(self, obj):
        related_user = obj.developer
        return related_user.position
    position.short_description = 'Должность'

    def about_me(self, obj):
        related_user = obj.developer
        return related_user.about_me
    about_me.short_description = 'О себе'

    def social_links(self, obj):
        return obj.developer.social

    social_links.short_description = 'Социальные сети'

    readonly_fields = ('email', 'position', 'about_me')
