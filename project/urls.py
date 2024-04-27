from django.urls import include, path
from rest_framework.routers import SimpleRouter

from project.views import ProjectListDetailView, DeveloperListDetailView

router = SimpleRouter()

router.register('', ProjectListDetailView)

urlpatterns = [
    path('developer/', DeveloperListDetailView.as_view({'get': 'list'})),
    path('developer/<int:pk>', DeveloperListDetailView.as_view({'get': 'retrieve'}))
] + router.urls