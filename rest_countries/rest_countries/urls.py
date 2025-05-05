"""
URL configuration for rest_countries project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.contrib.auth import views as auth_views
from django.urls import path, include
from core.api.views import CountryViewSet
from rest_framework.routers import DefaultRouter
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.urls import reverse_lazy

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'countries', CountryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('core.urls')),
    path('accounts/register/',
        RegistrationView.as_view(success_url=reverse_lazy('country-list'), template_name='registration/register.html'),
        name='django_registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/login/', LoginView.as_view(success_url=reverse_lazy('country-list'), template_name='registration/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/password_reset/', PasswordResetView.as_view(), name='password_reset'),
]
