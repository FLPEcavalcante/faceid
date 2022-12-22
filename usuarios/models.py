from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    id = models.ForeignKey(
        on_delete=True,
        to=True,
        max_length=64,
        primary_key=True,
    )
    name = models.CharField(
        max_length=255,
    )
    registration = models.CharField(
        max_length=255,
    )
    cep = models.CharField(
        max_length=8, blank=True
    )
    rua = models.CharField(
        max_length=100, blank=True
    )
    numero = models.IntegerField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return (Users)

    class Meta:
        verbose_name = 'User'


class ChangeLogs(models.Model):
    id = models.CharField(
        max_length=64,
    )
    operation_type = models.CharField(
        max_length=255,
    )
    table_name = models.CharField(
        max_length=255,
    )
    table_id = models.CharField(
        max_length=255,
    )
    timestamp = models.CharField(
        max_length=255,
    )


class Templates(models.Model):
    id = models.ForeignKey(
        max_length=64,
        primary_key=True,
    )
