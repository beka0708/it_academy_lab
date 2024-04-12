from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="ITLab",
        default_version='v1',
        description=f"""
      EXAMPLE REGISTER
      {{
          "username": "john",
          "email": "john@gmail.com",
          "password": "bastard123",
          "password2": "bastard123"
      }}

      LOGIN
      {{
          "email": "john@gmail.com",
          "password": "bastard123"
      }}
      """
        ,
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('docs<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
