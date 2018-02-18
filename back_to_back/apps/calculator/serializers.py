import datetime

from rest_framework import serializers

from .models import Calculation


class CalculationSerializer(serializers.ModelSerializer):
    datetime = serializers.SerializerMethodField()

    def get_datetime(self, calculation):
        return datetime.datetime.now()

    class Meta:
        model = Calculation
        fields = (
            'datetime',
            'value',
            'number',
            'occurrences',
            'last_occurrence',
        )
