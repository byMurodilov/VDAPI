from rest_framework import serializers
from .models import Veedeo

class VdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veedeo
        fields = '__all__'

    def create(self, validated_data):
        return Veedeo.objects.create(**validated_data)
