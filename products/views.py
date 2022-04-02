from itertools import chain
from django.shortcuts import render

from .models import Dishes, Wines, Bundle


def products(request):
    """ products view """

    dishes = Dishes.objects.all()
    wines = Wines.objects.all()
    bundles = Bundle.objects.all()

    all_products = list(chain(dishes, wines, bundles))

    context = {
        'dishes': dishes,
        'wines': wines,
        'bundles': bundles,
        'all_products': all_products,
    }

    return render(
        request,
        'products/products.html',
        context,
        )
