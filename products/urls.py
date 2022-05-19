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
        'dish_categories/',
        views.dish_category,
        name='dish_category'
    ),
    path(
        'wine_categories/',
        views.wine_category,
        name='wine_category'
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
    path(
        'delete/works/<int:product_id>',
        views.delete__works_product,
        name='delete__works_product'
    ),
    path(
        'delete/dish_category/<int:category_id>',
        views.delete_dish_category,
        name='delete_dish_category'
    ),
    path(
        'edit-dish/<int:product_id>',
        views.edit_dish,
        name='edit_dish'
        ),
    path(
        'edit-wine/<int:product_id>',
        views.edit_wine,
        name='edit_wine'
        ),
    path(
        'edit-works/<int:product_id>',
        views.edit_works,
        name='edit_works'
        ),
    path(
        'edit_dish_category/<int:category_id>',
        views.edit_dish_category,
        name='edit_dish_category'
        ),
    path(
        'edit_wine_category/<int:category_id>',
        views.edit_wine_category,
        name='edit_wine_category'
        ),
]
