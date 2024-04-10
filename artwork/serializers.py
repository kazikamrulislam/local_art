from rest_framework import serializers
from .models import Artwork
from django.conf import settings
from django.db import models

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('artist_name', 'bio')

class ArtworkSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(many=True)
    class Meta:
        model = Artwork
        fields = '__all__'