from rest_framework import serializers
from .models import ShortURL

class ShortenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ['original_url']
