from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from .models import Envelope
from .serializers import EnvelopeSerializer

class EnvelopeList(ListCreateAPIView):

    serializer_class = EnvelopeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Envelope.objects.filter(owner=self.request.user)

class EnvelopeDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = EnvelopeSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Envelope.objects.filter(owner=self.request.user)