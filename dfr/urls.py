
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('kemri/users/', admin.site.urls),
    path('', include('accounts.urls')),

]

admin.site.site_header = 'Kemri Users'

