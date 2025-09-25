from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def counts_summary(request):
    return Response({
        "total_records": 0,
        "total_patients": 0, 
        "total_organisms": 0,
        "message": "API endpoint ready - add data logic here"
    })

@api_view(['GET'])
def time_trends(request):
    period = request.GET.get('period', 'month')
    return Response({
        "period": period,
        "trends": [],
        "message": f"Time trends for {period}"
    })

@api_view(['GET'])
def options(request):
    return Response({
        "facilities": [],
        "organisms": [],
        "antibiotics": [],
        "message": "Options endpoint ready"
    })
