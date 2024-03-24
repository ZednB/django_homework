from django.urls import path
from users.apps import UsersConfig
from users.views import UserLoginView, UserLogoutView, RegisterView, UserUpdateView, generate_new_password
from django.views.generic import TemplateView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('update/', UserUpdateView.as_view(), name='update'),
    path('password_reset_form/', generate_new_password, name='password_reset_form'),
    path('password_reset_complete/',
         TemplateView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]