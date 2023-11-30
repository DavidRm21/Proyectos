from rest_framework import serializers, pagination

from .models import(
    Country
)

class CountrysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('__all__')