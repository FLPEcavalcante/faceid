from django.contrib import admin

from . import models


class AuthenticationAdmin(admin.ModelAdmin):
    """Auth model admin."""
    list_display = ('username', 'is_active',)
    list_filter = ('username', 'is_active', )
    search_fields = ('username', )


admin.site.register(models.Authentication, AuthenticationAdmin)
# Register your models here.
