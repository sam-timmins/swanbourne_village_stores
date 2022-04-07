from django.urls import path
from . import views

urlpatterns = [
    path('', views.the_menu, name='the_menu'),
    path('wine_store/', views.wine_store, name='wine_store'),
    path('the_freezer/', views.the_freezer, name='the_freezer'),
    path('fresh_food/', views.fresh_food, name='fresh_food'),
    path('the_works/', views.the_works, name='the_works'),
    path('<product_id>', views.product_detail_dishes, name='product_detail_dishes'),
    path('wine_store/<product_id>', views.product_details_wines, name='product_details_wines'),
    path('the_works/<product_id>', views.product_details_bundles, name='product_details_bundles'),
]
