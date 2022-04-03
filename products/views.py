from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Dishes, Wines


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


def wine_store(request):
    """ Menu view populating only the wines model with pagination """

    wines = Wines.objects.all()

    paginator = Paginator(wines, 24)

    page_number = request.GET.get('page')
    page_all_products = paginator.get_page(page_number)
    number_of_pages = 'a' * page_all_products.paginator.num_pages

    context = {
        'wines': wines,
        'page_all_products': page_all_products,
        'number_of_pages': number_of_pages,
    }

    return render(
        request,
        'products/wine-store.html',
        context,
        )


def the_freezer(request):
    """ Menu view populating only the frozen foods in the
    dishes model with pagination
    """

    dishes = Dishes.objects.all().filter(status=False)

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
        'products/the-freezer.html',
        context,
        )


def fresh_food(request):
    """
    Menu view populating only the fresh foods in the dishes
    model with pagination
    """

    dishes = Dishes.objects.all().filter(status=True)

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
        'products/fresh-food.html',
        context,
        )
