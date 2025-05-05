from django.db.models import QuerySet, Count

from .models import Language

class CountryService:

    @staticmethod

    def get_filtered_countries(queryset, search_query=None, region=None, language=None):
        
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        if region:
            queryset = queryset.filter(region__name__iexact=region)
        if language:
            queryset = queryset.filter(languages__code__iexact=language)
        return queryset.order_by('name')

    @staticmethod
    def get_regional_countries(country):
       
        return (
            country.region.countries.all()
            .exclude(pk=country.pk)
            .order_by('name')
        )

    @staticmethod
    def get_country_details(country):
        
        regional_countries = CountryService.get_regional_countries(country)
        
        # Get languages with country count
        languages = Language.objects.annotate(
        country_count=Count('countries')
        ).values('code', 'name', 'country_count')
        # print(languages)    
        languages_for_country = languages.filter(countries=country).values('code', 'name', 'country_count')
        # print(languages_for_country)
        return {
            'country': country,
            'regional_countries': regional_countries,
            'languages': languages_for_country,
            'population_formatted': f"{country.population:,}",
            'timezones': country.timezones,
            'region_countries_count': regional_countries.count() + 1  # Include current country
        }