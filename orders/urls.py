from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name='orders'),
    path('order_details/<order_number>',
         views.order_details,
         name='order_details'
         ),
    path(
        "order/delete/<order_number>",
        views.delete_order,
        name="delete_order"
        ),
    path(
        "collection_days/",
        views.collection_days,
        name="collection_days"
        ),
]
