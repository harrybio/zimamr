from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({"message": "ZimAMR API is running!", "status": "success"})

def counts_summary(request):
    return JsonResponse({"total_records": 1500, "status": "success"})

def time_trends(request):
    period = request.GET.get('period', 'month')
    return JsonResponse({"period": period, "data": [], "status": "success"})

def options(request):
    return JsonResponse({"facilities": [], "organisms": [], "status": "success"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root),
    path('api/summary/counts-summary/', counts_summary),
    path('api/summary/time-trends/', time_trends),
    path('api/options/', options),
]
