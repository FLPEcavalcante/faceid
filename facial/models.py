from django.db import models


class DataRequest(models.Model):
    """Data response Model in Json.

    Args:
        models (dict): Adding data the response. 

    Returns:
        JSON: Return a response data in JSON.
    """

    id = models.CharField(
        max_length=60,
        primary_key=True,
    )

    thumbnail = models.CharField(
        max_length=255,

    )

    fullframe = models.CharField(
        max_length=255,
    )

    matched = models.BooleanField(
        default=True
    )

    created_date = models.DateTimeField(null=True, blank=True)

    facial_creation_date = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        """Meta class for DataRequest model."""
        verbose_name = 'Data'
        verbose_name_plural = 'Data Request'

    def __str__(self):
        """DataRequest model data id representation."""
        return f'{self.id}'
