from django.contrib import admin

from .models import DishesCategory, WineCategory, Dishes, Wines


@admin.register(DishesCategory)
class DishesCategoryAdmin(admin.ModelAdmin):
    """ Settings for dishes categories in admin """
    search_fields = ['name']
    list_display = ('name', 'friendly_name')
    list_filter = ('name', 'friendly_name')


@admin.register(WineCategory)
class WineCategoryAdmin(admin.ModelAdmin):
    """ Settings for wine categories in admin """
    search_fields = ['name']
    list_display = ('name', 'friendly_name')
    list_filter = ('name', 'friendly_name')


@admin.register(Dishes)
class DishesAdmin(admin.ModelAdmin):
    """ Settings for dishes in admin """
    search_fields = ['name']
    list_display = ('name', 'category', 'price', 'status')
    list_filter = ('name', 'category', 'status')
    ordering = ['status', ]


@admin.register(Wines)
class WinesAdmin(admin.ModelAdmin):
    """ Settings for wines in admin """
    search_fields = ['name']
    list_display = ('name', 'category', 'price')
    list_filter = ('name', 'category')
    ordering = ['-category', 'name']
