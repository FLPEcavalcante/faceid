from django.contrib import admin

from . import models


class AuthenticationAdmin(admin.ModelAdmin):
    """Auth model admin."""

    list_display = ('username', 'is_active',)
    list_filter = ('username', 'is_active', )
    search_fields = ('username', )


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
admin.site.register(models.Authentication, AuthenticationAdmin)
admin.site.register(models.DataRequest, DataRequestAdmin)
