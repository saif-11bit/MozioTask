from rest_framework import serializers
from .models import (
    Provider,
    ServiceArea,
)

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = ["location"]


class ServiceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):
    locations = serializers.SerializerMethodField()
    class Meta:
        model = Provider
        fields = [
            'id',
            'name',
            'email',
            'phone_no',
            'language',
            'currency',
            'locations'
        ]
        
    def get_locations(self, obj):
        qs = ServiceArea.objects.filter(name=obj.id)
        qs_ser = LocationSerializer(qs, many=True)
        
        return qs_ser.data
