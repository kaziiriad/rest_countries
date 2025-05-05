from django.shortcuts import render, get_object_or_404
from .models import Country, Region, Language
from .api.views import CountryViewSet
from .utils import CountryService
from django.urls import reverse
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Count
from django.contrib.auth.decorators import login_required

@login_required
def country_list(request):
    """
    View to list all countries.
    """
    countries = Country.objects.all()
    regions = Region.objects.all()
    languages = Language.objects.all()

    search_query = request.GET.get('search', '')
    region_filter = request.GET.get('region', '')
    language_filter = request.GET.get('language', '')

    filtered_countries = CountryService.get_filtered_countries(
        countries, 
        search_query=search_query,
        region=region_filter,
        language=language_filter
    )
    # Pagination
    paginator = Paginator(filtered_countries, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'core/list.html', {
        'regions': regions,
        'languages': languages,
        'page_obj': page_obj,
        'search_query': search_query,
        'region_filter': region_filter,
        'language_filter': language_filter
    })
    

@login_required
def country_detail(request, pk):
    """
    View to display details of a specific country.
    """
    country = get_object_or_404(
        Country.objects.select_related('region').prefetch_related('languages'), 
        pk=pk
    )
    
    # Use shared service to get country details
    context = CountryService.get_country_details(country)
    
    return render(request, 'core/detail.html', context)
