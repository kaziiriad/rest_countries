from django.urls import path
from .api import views as api_views
from . import views as web_views

urlpatterns = [
    path('countries/', web_views.country_list, name='country-list'),
    path('countries/<int:pk>/', web_views.country_detail, name='country-detail'),
]