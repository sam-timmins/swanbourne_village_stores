from django.contrib import admin

from .models import DishesCategory, WineCategory, Dishes, Wines, Bundle


@admin.register(DishesCategory)
class DishesCategoryAdmin(admin.ModelAdmin):
    """ Settings for dishes categories in admin """
    search_fields = ['name']
    list_display = ('friendly_name', 'name', 'origin')
    list_filter = ('name', 'friendly_name', 'origin')


@admin.register(WineCategory)
class WineCategoryAdmin(admin.ModelAdmin):
    """ Settings for wine categories in admin """
    search_fields = ['name']
    list_display = ('friendly_name', 'variety', 'origin')
    list_filter = ('name', 'friendly_name', 'variety', 'origin')


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


@admin.register(Bundle)
class BundleAdmin(admin.ModelAdmin):
    """ Settings for bundles in admin """
    search_fields = ['name', ]
    list_display = ('name', 'wine', 'dish')
    list_filter = ('name', )
    ordering = ['name', ]
