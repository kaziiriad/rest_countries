from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Country
from .serializers import CountrySerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    filterset_fields = ['region__name', 'languages__code']

    @action(detail=True, methods=['get'])
    def regional(self, request, pk=None):
        country = self.get_object()
        regional_countries = Country.objects.filter(region=country.region).exclude(id=country.id)
        serializer = self.get_serializer(regional_countries, many=True)
        return Response(serializer.data)
