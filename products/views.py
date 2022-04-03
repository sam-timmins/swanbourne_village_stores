from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Dishes


def the_menu(request):
    """ Menu view populating only the dishes model with pagination """

    dishes = Dishes.objects.all().order_by('-status')

    paginator = Paginator(dishes, 24)

    page_number = request.GET.get('page')
    page_all_products = paginator.get_page(page_number)
    number_of_pages = 'a' * page_all_products.paginator.num_pages

    context = {
        'dishes': dishes,
        'page_all_products': page_all_products,
        'number_of_pages': number_of_pages,
    }

    return render(
        request,
        'products/the-menu.html',
        context,
        )
