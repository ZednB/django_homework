from django.urls import path
from catalof.views import home, contacts

urlpatterns = [
    path('', home),
    path('', contacts)
]