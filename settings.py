# settings.py
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'your-email@gmail.com' # email
EMAIL_HOST_PASSWORD = 'your-password' # пароль
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
