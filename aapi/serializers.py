from rest_framework import serializers

from aapi.models import Recebedor


class RecebedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recebedor
        fields = '__all__'

