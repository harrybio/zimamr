from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET'])
def counts_summary(request): return Response({"message": "API ready"})
@api_view(['GET'])  
def time_trends(request): return Response({"period": request.GET.get('period', 'month')})
@api_view(['GET'])
def options(request): return Response({"options": []})
