from rest_framework import serializers

from social.models import News, NewsImage, AboutUs, AboutUsImages, Gallery


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class NewsListSerializer(serializers.ModelSerializer):
    preview = GallerySerializer(read_only=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'short_body', 'preview', 'speaker', 'created_at')


class NewsImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = ('image', 'title')


class NewsDetailSerializer(serializers.ModelSerializer):
    images = NewsImagesSerializer(many=True, read_only=True)
    latest_news = serializers.SerializerMethodField()

    class Meta:
        model = News
        exclude = ('preview',)

    def get_latest_news(self, obj):
        latest_news = News.objects.exclude(pk=obj.pk).order_by('-created_at')[:4]
        serializer = NewsListSerializer(instance=latest_news, many=True)
        return serializer.data


class AboutUsImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsImages
        fields = ['images']


class AboutUsSerializer(serializers.ModelSerializer):
    images = AboutUsImagesSerializer(many=True, read_only=True)

    class Meta:
        model = AboutUs
        fields = ['body', 'images']