from rest_framework import serializers
from .models import Envelope

class EnvelopeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Envelope
        fields = ['id', 'name', 'description', 'balance']