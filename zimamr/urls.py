from django.contrib import admin
from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request):
    return Response({"message": "ZimAMR API is running!"})

@api_view(['GET'])
def counts_summary(request):
    return Response({"total_records": 0, "message": "Counts summary ready"})

@api_view(['GET'])
def time_trends(request):
    period = request.GET.get('period', 'month')
    return Response({"period": period, "trends": []})

@api_view(['GET'])
def options(request):
    return Response({"facilities": [], "organisms": []})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root),
    path('api/summary/counts-summary', counts_summary),
    path('api/summary/time-trends', time_trends),
    path('api/options', options),
]
