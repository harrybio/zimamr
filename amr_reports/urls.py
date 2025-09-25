from django.urls import path
from . import views
urlpatterns = [
    path('summary/counts-summary/', views.counts_summary),
    path('summary/time-trends/', views.time_trends),
    path('options/', views.options),
]
