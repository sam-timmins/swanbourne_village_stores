from django.contrib import admin

from .models import CollectionDays, Order


@admin.register(CollectionDays)
class CollectionDaysAdmin(admin.ModelAdmin):
    """ Settings for collection days in admin """
    search_fields = ['day']
    list_display = ('day',)
    list_filter = ('day',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """ Settings for orders in admin """
    list_display = (
        'date',
        'order_number',
        'full_name',
        'email',
        'phone_number',
        'collection_day'
        )
