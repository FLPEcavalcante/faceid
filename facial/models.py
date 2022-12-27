from django.db import models


class Authentication(models.Model):

    username = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    password = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        verbose_name = 'Auth'
        verbose_name_plural = 'Authentications'

    def __str__(self):
        return f'{self.username}'
