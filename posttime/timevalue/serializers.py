from rest_framework import serializers
from .models import TimeValueAggregated


class TimeValueAggregatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeValueAggregated
        fields = ('minute', 'avg_value')
