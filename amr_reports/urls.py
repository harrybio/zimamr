from django.urls import path
from . import views

urlpatterns = [
    path('summary/counts-summary', views.counts_summary, name='counts-summary'),
    path('summary/time-trends', views.time_trends, name='time-trends'),
    path('options', views.options, name='options'),
]
