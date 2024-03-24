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
    path('new_password/', generate_new_password, name='generate_new_password'),
    path('new_password_info/', TemplateView.as_view(template_name='users/new_password_info.html'), name='new_password_info'),
]