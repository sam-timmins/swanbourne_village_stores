from django.urls import path
from . import views

urlpatterns = [
    path('', views.the_menu, name='the_menu'),
]
