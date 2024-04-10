from django.shortcuts import render
from .models import Artwork
from .serializers import ArtworkSerializer
from rest_framework import generics, permissions



class ArtworkListCreate(generics.ListCreateAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(artist=self.request.user)

class ArtworkDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(artist=self.request.user)