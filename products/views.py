from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Dishes, Wines, Bundle


def the_menu(request):
    """ 
    Menu view populating only the dishes model with pagination.
    Search bar queries the the dishes model based on the dish
    name or description
    """

    dishes = Dishes.objects.all().order_by('-status')

    paginator = Paginator(dishes, 24)

    page_number = request.GET.get('page')
    page_all_products = paginator.get_page(page_number)
    number_of_pages = 'a' * page_all_products.paginator.num_pages

    query = None

    if request.GET:
        if 'main-search-query' in request.GET:
            query = request.GET['main-search-query']
            if not query:
                return redirect(reverse('the_menu'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            dishes = dishes.filter(queries)

    context = {
        'dishes': dishes,
        'page_all_products': page_all_products,
        'number_of_pages': number_of_pages,
        'search': query,
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


def the_works(request):
    """
    Menu view populating only the bundle packages in the bundle
    model with pagination. Calculates the saving of each field
    in the bundle model
    """

    bundle = Bundle.objects.all()

    paginator = Paginator(bundle, 24)

    page_number = request.GET.get('page')
    page_all_products = paginator.get_page(page_number)
    number_of_pages = 'a' * page_all_products.paginator.num_pages

    for item in bundle:
        wine_cost = item.wine.price
        dish_cost = item.dish.price

        before_cost = wine_cost + dish_cost
        saving = before_cost - item.price

    context = {
        'bundle': bundle,
        'before_cost': before_cost,
        'saving': saving,
        'page_all_products': page_all_products,
        'number_of_pages': number_of_pages,
    }

    return render(
        request,
        'products/the-works.html',
        context,
        )


def product_detail_dishes(request, product_id):
    """ Detailed individual view of a product """
    dishes = Dishes.objects.all()

    product = get_object_or_404(Dishes, pk=product_id)

    context = {
        'product': product,
        'dishes': dishes,
    }
    return render(
        request,
        'products/product-details.html',
        context,
        )


def product_details_wines(request, product_id):
    """ Detailed individual view of a wine product """
    wines = Wines.objects.all()

    product = get_object_or_404(Wines, pk=product_id)

    context = {
        'product': product,
        'wines': wines,
    }
    return render(
        request,
        'products/product-details.html',
        context,
        )


def product_details_bundles(request, product_id):
    """ Detailed individual view of a wine product """
    bundle = Bundle.objects.all()

    product = get_object_or_404(Bundle, pk=product_id)

    context = {
        'product': product,
        'bundle': bundle,
    }
    return render(
        request,
        'products/product-details.html',
        context,
        )
