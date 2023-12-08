from rest_framework import serializers

from ..models import Societe, ModelAvion

class AddAvionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ModelAvion
        fields = ['name', 'typeAir', 'typeOfFuel', 'capacityOfFuel', 'Altitude', 'societe', 'created_at']
        extra_kwargs = {
            'created_at': {'read_only': True}
        }