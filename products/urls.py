from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.the_menu,
        name='the_menu'
        ),
    path(
        'wine_store/',
        views.wine_store,
        name='wine_store'
        ),
    path(
        'the_freezer/',
        views.the_freezer,
        name='the_freezer'
        ),
    path(
        'fresh_food/',
        views.fresh_food,
        name='fresh_food'
        ),
    path(
        'the_works/',
        views.the_works,
        name='the_works'
        ),
    path(
        '<int:product_id>',
        views.product_detail_dishes,
        name='product_detail_dishes'
        ),
    path(
        'wine_store/<int:product_id>',
        views.product_details_wines,
        name='product_details_wines'
        ),
    path(
        'the_works/<int:product_id>',
        views.product_details_bundles,
        name='product_details_bundles'
        ),
    path(
        'create_dish/',
        views.create_dish,
        name='create_dish'
    ),
    path(
        'create_wine/',
        views.create_wine,
        name='create_wine'
    ),
    path(
        'create_works/',
        views.create_works,
        name='create_works'
    ),
    path(
        'delete/dish/<int:product_id>',
        views.delete__dish_product,
        name='delete__dish_product'
    ),
        path(
        'delete/wine/<int:product_id>',
        views.delete__wine_product,
        name='delete__wine_product'
    ),
]
