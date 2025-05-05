from rest_framework import serializers
from ..models import Country


class CountrySerializer(serializers.ModelSerializer):
    region = serializers.StringRelatedField()
    languages = serializers.SlugRelatedField(many=True, slug_field='code', read_only=True)

    class Meta:
        model = Country
        fields = ['id', 'name', 'cca2', 'capital', 'population', 'timezones', 'flag_url', 'region', 'languages']
