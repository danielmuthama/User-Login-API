
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('moringa/admin', admin.site.urls),
    path('', include('accounts.urls')),
]

admin.site.site_header = 'Moringa Hosp.-Users'

