from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from .models import Account
from .serializers import AccountSerializer

class AccountList(ListCreateAPIView):

    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Account.objects.filter(owner=self.request.user)

class AccountDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Account.objects.filter(owner=self.request.user)