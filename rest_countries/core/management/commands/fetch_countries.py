from django.core.management.base import BaseCommand
import requests
from core.models import Country, Region, Language

class Command(BaseCommand):
    help = 'Fetches country data from REST Countries API'

    def handle(self, *args, **kwargs):
        response = requests.get('https://restcountries.com/v3.1/all')
        data = response.json()

        # check if database is empty
        if Country.objects.exists():
            self.stdout.write(self.style.WARNING('Database already populated. Exiting...'))
            return
        self.stdout.write(self.style.SUCCESS('Fetching country data...'))
        self.stdout.write(self.style.SUCCESS('Creating countries...'))
        self.stdout.write(self.style.SUCCESS('Creating regions...'))
        self.stdout.write(self.style.SUCCESS('Creating languages...'))

        for country_data in data:
            # Extract data
            name = country_data.get('name', {}).get('common', '')
            cca2 = country_data.get('cca2', '').lower()
            capital = country_data.get('capital', [''])[0] if country_data.get('capital') else None
            population = country_data.get('population', 0)
            timezones = country_data.get('timezones', [])
            flag_url = country_data.get('flags', {}).get('png', '')
            region_name = country_data.get('region', '')
            languages = country_data.get('languages', {}).keys()

            # Get or create Region
            region, _ = Region.objects.get_or_create(name=region_name) if region_name else (None, None)

            # Create Country
            country = Country.objects.create(
                name=name,
                cca2=cca2,
                capital=capital,
                population=population,
                timezones=timezones,
                flag_url=flag_url,
                region=region
            )

            # Add Languages
            for lang_code in languages:
                lang_name = country_data['languages'][lang_code]
                lang, _ = Language.objects.get_or_create(code=lang_code, defaults={'name': lang_name})
                country.languages.add(lang)
