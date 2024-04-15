from django.urls import include, path
from rest_framework.routers import DefaultRouter

from social.views import NewsRetrieveListViewSet, AboutsUsViewSet

router = DefaultRouter()
router.register('news', NewsRetrieveListViewSet)
router.register('aboutus', AboutsUsViewSet)


urlpatterns = [
    path('', include(router.urls))
]