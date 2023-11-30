from rest_framework import serializers, pagination

from .models import(
    LanguageInfo
)

class LanguageInfosSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageInfo
        fields = ('__all__')