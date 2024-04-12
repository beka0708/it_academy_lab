from django.contrib import admin
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import path, reverse

from account.send_mail import send_confirmation_email
from account.utils import generate_unique_password
from .models import Review, Student, Client
from django.contrib import messages


User = get_user_model()

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'created_at', 'rating', 'truncated_body')
    search_fields = ('user',)
    list_filter = ('created_at',)

    def full_name(self, obj):
        return obj.user.full_name

    def truncated_body(self, obj):
        return f'{obj.body[:30]}...' if obj.body else ''

    full_name.short_description = "ФИО"
    truncated_body.short_description = "Комментарий"


class StudentAdmin(admin.ModelAdmin):
    class Meta:
        model = Student

    list_display = ('full_name', 'email', 'phone_number', 'status')
    list_filter = ('status',)

    def get_urls(self):
        urls = super(StudentAdmin, self).get_urls()
        custom_urls = [
            path('get_student/<int:object_id>/', self.admin_site.admin_view(self.get_student), name='get_student'), ]
        return custom_urls + urls

    def get_student(self, request, object_id):
        student = Student.objects.get(pk=object_id)
        student.status = 'approved'  # Изменяем статус студента
        student.save()
        password = generate_unique_password()
        existing_user = User.objects.filter(email=student.email).exists()
        if existing_user:
            messages.error(request, f"Пользователь с email {student.email} уже существует!")
            return redirect('admin:form_student_changelist')

        user = User.objects.create_user(
            role='student',
            full_name=student.full_name,
            email=student.email,
            position=student.position,
            phone_number=student.phone_number,
            password=password,
        )
        send_confirmation_email(student.email, password)
        user.save()

        change_list_url = reverse('admin:form_student_changelist')
        return redirect(change_list_url)


class ClientAdmin(admin.ModelAdmin):
    class Meta:
        model = Client

    list_display = ('full_name', 'email', 'phone_number', 'company', 'status')
    list_filter = ('status',)


    def get_urls(self):
        urls = super(ClientAdmin, self).get_urls()
        custom_urls = [
            path('get_student/<int:object_id>/', self.admin_site.admin_view(self.get_client), name='get_client'), ]
        return custom_urls + urls

    def get_client(self, request, object_id):
        client = Client.objects.get(pk=object_id)
        client.status = 'approved'  # Изменяем статус клиента
        client.save()
        password = generate_unique_password()
        existing_user = User.objects.filter(email=client.email).exists()
        if existing_user:
            messages.error(request, f"Пользователь с email {client.email} уже существует!")
            return redirect('admin:form_client_changelist')

        user = User.objects.create_user(
            role='client',
            full_name=client.full_name,
            email=client.email,
            phone_number=client.phone_number,
            company=client.company,
            password=password,
        )
        send_confirmation_email(client.email, password)
        user.save()

        change_list_url = reverse('admin:form_client_changelist')
        return redirect(change_list_url)


admin.site.register(Client, ClientAdmin)
admin.site.register(Student, StudentAdmin)
