from django.contrib import admin

from . import models


class DataRequestAdmin(admin.ModelAdmin):
    """Data model admin."""

    list_display = (
        'id',
        'matched',
        'created_date',
        'facial_creation_date',
        'fullframe',
    )

    list_filter = (
        'created_date',
        'facial_creation_date'
    )

    readonly_fields = ('facial_creation_date',)

    search_fields = ('id',)


# Register your models here.
admin.site.register(models.DataRequest, DataRequestAdmin)
