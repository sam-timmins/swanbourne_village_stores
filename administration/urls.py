from django.urls import path
from . import views


urlpatterns = [
    path('', views.administration, name='administration'),
    path(
        'dishes/',
        views.dishes,
        name='dishes'
    ),
    path(
        'delete/dish/<int:dish_id>',
        views.delete_dish_product,
        name='delete_dish_product'
    ),
]
