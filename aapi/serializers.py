from rest_framework import serializers

from aapi.models import Recebedor
from django.contrib.auth.models import User

class RecebedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recebedor
        fields = '__all__'

