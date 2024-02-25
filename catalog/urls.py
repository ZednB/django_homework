from django.urls import path
from catalog.views import home, contacts, base

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('base/<int:pk>/', base, name='base')
]
