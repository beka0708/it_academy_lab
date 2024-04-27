from django.urls import path, include

from rest_framework import routers

from account.views import UserModelViewSet, SocialLinksUpdateViewSet

router = routers.DefaultRouter()
router.register('', UserModelViewSet)
router.register('links', SocialLinksUpdateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]