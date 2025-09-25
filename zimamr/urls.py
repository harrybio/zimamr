"""zimamr URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({"message": "ZimAMR API is running!"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/auth/', include('rest_framework.urls')),
]
