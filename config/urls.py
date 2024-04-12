
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .drf_swagger import urlpatterns as swagger_urlpatterns

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    #My_urls
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('social/', include('social.urls')),
    path('form/', include('form.urls')),
    path('project/', include('project.urls')),

                  #password reset ulr
    path('api/password_reset/', include('django_rest_passwordreset.urls')),

    #JWT-Token_urls
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

] + swagger_urlpatterns


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

