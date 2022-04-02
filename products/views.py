from itertools import chain
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Dishes, Wines, Bundle


def products(request):
    """ Products view with pagination"""

    dishes = Dishes.objects.all()
    wines = Wines.objects.all()
    bundles = Bundle.objects.all()

    all_products = list(chain(dishes, wines))

    paginator = Paginator(all_products, 24)

    page_number = request.GET.get('page')
    page_all_products = paginator.get_page(page_number)

    context = {
        'dishes': dishes,
        'wines': wines,
        'bundles': bundles,
        'all_products': all_products,
        'page_all_products': page_all_products,
    }

    return render(
        request,
        'products/products.html',
        context,
        )
