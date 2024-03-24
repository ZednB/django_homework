from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView
from users.models import User
from django.urls import reverse_lazy, reverse
from users.forms import UserRegisterForm, UserForm
from django.core.mail import send_mail
from django.conf import settings
import random
from django.contrib.auth.hashers import make_password


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('catalog:base')


class UserLogoutView(LogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Поздравляем с регистрацией.',
            message='Вы зарегистрировались на нашей платформе.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email],
        )
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:update')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
            send_mail(
                subject='Вы сменили пароль',
                message=f'Ваш новый пароль - {new_password}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
            )
            user.set_password(new_password)
            user.save()
            return redirect(reverse('users:password_reset_complete'))
        except User.DoesNotExist:
            return render(request, 'users/password_reset_form.html',
                          {'error': 'Пользователь с такой почтой не найден.'})
    else:
        return render(request, 'users/password_reset_form.html')
