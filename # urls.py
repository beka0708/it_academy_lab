urls.py
from django.urls import path
from .views import RegisterView, activate_account

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/activate/<token>/', activate_account),
    # Swagger UI 
    path('swagger/', get_schema_view(
        title="User Registration API",
        description="API for registering users and activating their accounts.",
        version="1.0.0",
    ), name='schema-swagger-ui'),
    path('swagger.json/', swagger_auto_schema.get_swagger_view(), name='schema-json'),
]
