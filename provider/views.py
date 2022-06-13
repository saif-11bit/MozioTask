from rest_framework import viewsets, mixins, views, status
from .models import (
    Provider,
    ServiceArea
)
from .serializers import (
    ProviderSerializer,
    ServiceAreaSerializer,
)
from rest_framework.response import Response


class ProviderViewset(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ServiceAreaViewset(viewsets.ModelViewSet):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer


class LocateProvider(views.APIView):
    
    def get(self, request):
        data = self.request.query_params
        print(data)
        lon = data.get('lon')
        lat = data.get('lat')
        if lon != None and lat != None:
            coordinates = [float(lat),float(lon)]
            service_areas = ServiceArea.objects.filter(location__contains=coordinates)
            serializer = ServiceAreaSerializer(service_areas, many=True)       
            return Response({"data": serializer.data})
        else:
            return Response({"error": "please provide lat and lon"})