from django.contrib import admin

from .models import DishesCategory


@admin.register(DishesCategory)
class DishesCategoryAdmin(admin.ModelAdmin):
    """ Settings for dishes categories in admin """
    search_fields = ['name']
    list_display = ('name', 'friendly_name')
    list_filter = ('name', 'friendly_name')
