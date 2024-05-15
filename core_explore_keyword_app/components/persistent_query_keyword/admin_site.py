""" Custom admin site for the Persistent Query Keyword model
"""
from django.contrib import admin


class CustomPersistentQueryKeywordAdmin(admin.ModelAdmin):
    """CustomPersistentQueryKeywordAdmin"""

    exclude = ["data_sources"]
    list_display = ["name", "user_id", "creation_date"]
    search_fields = ["name"]

    def has_add_permission(self, request, obj=None):
        """Prevent from manually adding Persistent Queries"""
        return False
