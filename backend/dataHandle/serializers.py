from rest_framework import serializers
from .models import carsList

class carSerializer(serializers.ModelSerializer):
    class Meta:
        model = carsList
        fields = ["ownerName", "ownerPhone", "ownerAddress", "carModel", "carRent", "carImage"]