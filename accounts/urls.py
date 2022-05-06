from .views import RegisterAPI
from django.urls import path

urlpatterns = [
    path('kemri/api/register/', RegisterAPI.as_view(), name='register'),
]
