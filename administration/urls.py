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
        'wines/',
        views.wines,
        name='wines'
    ),
    path(
        'the_works/',
        views.works,
        name='works'
    ),
    path(
        'delete/dish/<int:dish_id>',
        views.delete_dish_product,
        name='delete_dish_product'
    ),
    path(
        'delete/wine/<int:wine_id>',
        views.delete_wine_product,
        name='delete_wine_product'
    ),
    path(
        'delete/works/<int:works_id>',
        views.delete_works_product,
        name='delete_works_product'
    ),
    path(
        'edit-dish/<int:dish_id>',
        views.edit_dish,
        name='edit_dish'
        ),
    path(
        'edit-wine/<int:wine_id>',
        views.edit_wine,
        name='edit_wine'
        ),
    path(
        'edit-works/<int:works_id>',
        views.edit_works,
        name='edit_works'
        ),
]
