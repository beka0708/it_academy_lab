from django.core.mail import send_mail
from decouple import config as de_config
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created

HOST = de_config('HOST')


def send_confirmation_email(email, password):
    send_mail(
        f'Здравствуйте, ваша заявка была одобрена!',
        f'Ваш логин и пароль следующие, сохраните пароль чтобы его не потерять!'
        f'Можете войти по ссылке http://{HOST}/login/\n'
        f'Логин: {email}\nПароль: {password}',
        de_config('EMAIL_USER'),
        [email],
        fail_silently=False,
    )


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = f"Привет,\n\nЧтобы сбросить пароль, перейдите по этой ссылке:\n\nhttp://{HOST}/api/password_reset/confirm/\n\n\tИ введите вот этот токен\t{reset_password_token.key}"

    send_mail(
        "Сброс пароля",
        email_plaintext_message,
        de_config('EMAIL_USER'),
        [reset_password_token.user.email],
)