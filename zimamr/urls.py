from django.contrib import admin
from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET'])
def api_root(request): return Response({"message": "ZimAMR API running!"})
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root),
    path('api/', include('amr_reports.urls')),
]
