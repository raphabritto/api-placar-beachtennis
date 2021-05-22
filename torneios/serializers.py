from rest_framework import serializers

from .models import Torneios


class TorneiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torneios
        fields = '__all__'