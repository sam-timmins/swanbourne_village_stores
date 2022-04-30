from django.contrib import admin

from .models import CollectionDays


@admin.register(CollectionDays)
class CollectionDaysAdmin(admin.ModelAdmin):
    """ Settings for collection days in admin """
    search_fields = ['day']
    list_display = ('day',)
    list_filter = ('day',)
