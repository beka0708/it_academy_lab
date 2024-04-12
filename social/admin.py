from django.contrib import admin
from .models import Gallery, News, NewsImage, AboutUs, AboutUsImages


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image',)
    search_fields = ('image',)


class NewsImageInline(admin.TabularInline):
    model = NewsImage


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'speaker', 'created_at', 'updated_at')
    search_fields = ('title', 'speaker', 'short_body', 'body')
    list_filter = ('created_at', 'updated_at', 'speaker')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title','short_body', 'body', 'speaker', 'preview')
        }),
        ('Дата и время', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    inlines = [NewsImageInline]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('preview',)
        return self.readonly_fields


class AboutUsImagesInline(admin.TabularInline):
    model = AboutUsImages
    verbose_name = "Изображение"
    verbose_name_plural = "Изображения"


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('body_',)
    search_fields = ('body',)
    inlines = [AboutUsImagesInline]

    def body_(self, obj):
        return f'{obj.body[:70]}...' if obj.body else ''

    body_.short_description = "Содержимое"






