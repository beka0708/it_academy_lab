from django.urls import path
from rest_framework.routers import SimpleRouter

from form.views import ClientCreateView, StudentCreateView, ReviewCreateListView

router = SimpleRouter()

router.register(r'client', ClientCreateView)
router.register(r'student', StudentCreateView)
router.register(r'review', ReviewCreateListView, basename='review')


urlpatterns = [
] + router.urls


