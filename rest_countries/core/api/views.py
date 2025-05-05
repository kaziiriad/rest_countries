from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from ..models import Country
from .serializers import CountrySerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 500


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    filterset_fields = ['region__name', 'languages__code']
    pagination_class = StandardResultsSetPagination

    @action(detail=True, methods=['get'])
    def regional(self, request, pk=None):
        country = self.get_object()
        regional_countries = Country.objects.filter(region=country.region).exclude(id=country.id)
        
        # Apply pagination to the regional countries queryset
        page = self.paginate_queryset(regional_countries)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
            
        serializer = self.get_serializer(regional_countries, many=True)
        return Response(serializer.data)
