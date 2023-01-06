from rest_framework import serializers

from . import models


class DataRequestSerializer(serializers.ModelSerializer):
    """A class to serialize Request Data."""

    class Meta:
        """Meta class for DataRequestSerializer."""

        model = models.DataRequest
        fields = '__all__'
