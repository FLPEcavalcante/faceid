from rest_framework import serializers
from .models import Authentication, DataRequest


class AuthenticationSerializer(serializers.ModelSerializer):
    """A class to serialize Authentication data."""
    class Meta:
        """Meta class for AuthenticationSerializer."""
        model = Authentication
        fields = '__all__'


class DataRequestSerializer(serializers.ModelSerializer):
    """A class to serialize Request Data."""
    class Meta:
        """Meta class for DataRequestSerializer."""
        model = DataRequest
        fields = '__all__'
