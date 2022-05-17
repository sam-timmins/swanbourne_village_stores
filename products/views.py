from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Dishes, Wines, Bundle, DishesCategory
from .forms import (DishForm, WineForm, WorksForm,
                    DishCategoryForm,)


def the_menu(request):
    """
    Menu view populating only the dishes model with pagination.
    Search bar queries the the dishes model based on the dish
    name or description
    """

    dishes = Dishes.objects.all().order_by('-status')

    dish_names = []

    for dish in dishes:
        dish_names.append(dish.name.title())

    dish_names = list(dict.fromkeys(dish_names))
    ordered_dish_names = sorted(dish_names)

    paginator = Paginator(dishes, 24)

    page_number = request.GET.get('page')
    page_all_products = paginator.get_page(page_number)
    number_of_pages = 'a' * page_all_products.paginator.num_pages

    query = None
    sort = None
    direction = None

    if request.GET:
        if 'main-search-query' in request.GET:
            query = request.GET['main-search-query']
            if not query:
                return redirect(reverse('the_menu'))

            queries = Q(
                name__icontains=query
                ) | Q(description__icontains=query)
            dishes = dishes.filter(queries)

        if 'menu-name-query' in request.GET:
            query = request.GET['menu-name-query']

            if not query or query == 'reset':
                return redirect(reverse('the_menu'))

            queries = Q(name__icontains=query)

            dishes = dishes.filter(queries)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                dishes = dishes.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            dishes = dishes.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'dishes': dishes,
        'page_all_products': page_all_products,
        'number_of_pages': number_of_pages,
        'search': query,
        'ordered_dish_names': ordered_dish_names,
        'current_sorting': current_sorting,
        'query': query,
    }

    return render(
        request,
        'products/the-menu.html',
        context,
        )


def wine_store(request):
    """ Menu view populating only the wines model with pagination """

    wines = Wines.objects.all()

    varieties = []

    for wine in wines:
        varieties.append(wine.category.friendly_name.title())

    varieties = list(dict.fromkeys(varieties))
    ordered_varieties = sorted(varieties)

    paginator = Paginator(wines, 24)

    page_number = request.GET.get('page')
    page_all_products = paginator.get_page(page_number)
    number_of_pages = 'a' * page_all_products.paginator.num_pages

    query = None
    sort = None
    direction = None

    if request.GET:

        if 'wine-category-query' in request.GET:
            query = request.GET['wine-category-query']

            if not query or query == 'reset':
                return redirect(reverse('wine_store'))

            queries = Q(category__friendly_name__icontains=query)

            wines = wines.filter(queries)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                wines = wines.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            wines = wines.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'wines': wines,
        'page_all_products': page_all_products,
        'number_of_pages': number_of_pages,
        'ordered_varieties': ordered_varieties,
        'current_sorting': current_sorting,
        'query': query,
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

    dish_names = []

    for dish in dishes:
        dish_names.append(dish.name.title())

    dish_names = list(dict.fromkeys(dish_names))
    ordered_dish_names = sorted(dish_names)

    paginator = Paginator(dishes, 24)

    page_number = request.GET.get('page')
    page_all_products = paginator.get_page(page_number)
    number_of_pages = 'a' * page_all_products.paginator.num_pages

    query = None
    sort = None
    direction = None

    if request.GET:

        if 'freezer-name-query' in request.GET:
            query = request.GET['freezer-name-query']

            if not query or query == 'reset':
                return redirect(reverse('the_freezer'))

            queries = Q(name__icontains=query)

            dishes = dishes.filter(queries)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                dishes = dishes.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            dishes = dishes.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'dishes': dishes,
        'page_all_products': page_all_products,
        'number_of_pages': number_of_pages,
        'ordered_dish_names': ordered_dish_names,
        'current_sorting': current_sorting,
        'query': query,
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

    dish_names = []

    for dish in dishes:
        dish_names.append(dish.name.title())

    dish_names = list(dict.fromkeys(dish_names))
    ordered_dish_names = sorted(dish_names)

    paginator = Paginator(dishes, 24)

    page_number = request.GET.get('page')
    page_all_products = paginator.get_page(page_number)
    number_of_pages = 'a' * page_all_products.paginator.num_pages

    query = None
    sort = None
    direction = None

    if request.GET:

        if 'fresh-name-query' in request.GET:
            query = request.GET['fresh-name-query']

            if not query or query == 'reset':
                return redirect(reverse('the_freezer'))

            queries = Q(name__icontains=query)

            dishes = dishes.filter(queries)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                dishes = dishes.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            dishes = dishes.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'dishes': dishes,
        'page_all_products': page_all_products,
        'number_of_pages': number_of_pages,
        'ordered_dish_names': ordered_dish_names,
        'current_sorting': current_sorting,
        'query': query,
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

    bundle_names = []

    for item in bundle:
        bundle_names.append(item.name.title())

    bundle_names = list(dict.fromkeys(bundle_names))
    ordered_bundle_names = sorted(bundle_names)

    paginator = Paginator(bundle, 24)

    page_number = request.GET.get('page')
    page_all_products = paginator.get_page(page_number)
    number_of_pages = 'a' * page_all_products.paginator.num_pages

    query = None
    sort = None
    direction = None

    if request.GET:

        if 'the-works-query' in request.GET:
            query = request.GET['the-works-query']

            if not query or query == 'reset':
                return redirect(reverse('the_works'))

            queries = Q(name__icontains=query)

            bundle = bundle.filter(queries)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                bundle = bundle.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            bundle = bundle.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'bundle': bundle,
        'page_all_products': page_all_products,
        'number_of_pages': number_of_pages,
        'ordered_bundle_names': ordered_bundle_names,
        'current_sorting': current_sorting,
        'query': query,
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


def create_dish(request):
    """ Add a dish to the store """
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            format_name = name.title()
            form.save()
            messages.success(request, f'Successfully created {format_name}')
            return redirect(reverse('create_dish'))
        else:
            messages.error(
                request,
                'Unable to create the dish. \
                Please ensure all fields are filled out correctly.'
                )
    else:
        form = DishForm()

    context = {
        'form': form,
    }

    return render(request, 'products/create-dish.html', context)


def create_wine(request):
    """ Add a wine to the store """
    if request.method == 'POST':
        form = WineForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            format_name = name.title()
            form.save()
            messages.success(request, f'Successfully created {format_name}')
            return redirect(reverse('create_wine'))
        else:
            messages.error(
                request,
                'Unable to create the wine. \
                Please ensure all fields are filled out correctly.'
                )
    else:
        form = WineForm()

    context = {
        'form': form,
    }

    return render(request, 'products/create-wine.html', context)


def create_works(request):
    """ Add a bundle to the store """
    if request.method == 'POST':
        form = WorksForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            format_name = name.title()
            form.save()
            messages.success(request, f'Successfully created {format_name}')
            return redirect(reverse('create_works'))
        else:
            messages.error(
                request,
                'Unable to create the combination. \
                Please ensure all fields are filled out correctly.'
                )
    else:
        form = WorksForm()

    context = {
        'form': form,
    }

    return render(request, 'products/create-works.html', context)


def dish_category(request):
    """ Create wine and dish categories """

    dishes_category_form = DishCategoryForm()
    categories = DishesCategory.objects.all()

    if request.method == 'POST':
        dishes_category_form = DishCategoryForm(request.POST)
        if dishes_category_form.is_valid():
            name = dishes_category_form.cleaned_data.get('name').title()
            dishes_category_form.save()
            messages.success(request, f'Successfully created {name}')
            return redirect(reverse('dish_category'))

    context = {
        'dishes_category_form': dishes_category_form,
        'categories': categories,
    }

    return render(request, 'products/categories.html', context)


@login_required
def delete_dish_category(request, category_id):
    """Delete dish category"""
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    category = get_object_or_404(DishesCategory, pk=category_id)
    category.delete()

    messages.success(request, 'The category has been deleted')
    return redirect(reverse('dish_category'))


@login_required
def delete__dish_product(request, product_id):
    """Delete dish product"""
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    product = get_object_or_404(Dishes, pk=product_id)
    product.delete()

    messages.success(request, 'The dish has been deleted from the store')
    return redirect(reverse('the_menu'))


@login_required
def delete__wine_product(request, product_id):
    """Delete wine product"""
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    product = get_object_or_404(Wines, pk=product_id)
    product.delete()

    messages.success(request, 'The wine has been deleted from the store')
    return redirect(reverse('wine_store'))


@login_required
def delete__works_product(request, product_id):
    """Delete works combination product"""
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    product = get_object_or_404(Bundle, pk=product_id)
    product.delete()

    messages.success(
        request,
        'The combination has been deleted from the store'
        )
    return redirect(reverse('the_works'))


def edit_dish(request, product_id):
    """ Edit the item in the dishes model """
    dishes = Dishes.objects.all()
    product = get_object_or_404(Dishes, pk=product_id)

    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.name}')
            return redirect(
                reverse(
                    'product_detail_dishes',
                    args=[product.id],
                    )
                )
        else:
            messages.error(
                request,
                f'Unable to update {product.name}. \
                Please ensure all fields are filled out correctly.'
                )
    else:
        form = DishForm()

    form = DishForm(instance=product)

    messages.info(request, f'You are currently editing {product.name}')

    context = {
        'form': form,
        'dishes': dishes,
        'product': product,
    }

    return render(
        request,
        'products/edit-product.html',
        context
        )


def edit_wine(request, product_id):
    """ Edit the item in the wines model """
    wines = Wines.objects.all()
    product = get_object_or_404(Wines, pk=product_id)

    if request.method == 'POST':
        form = WineForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.name}')
            return redirect(
                reverse(
                    'product_details_wines',
                    args=[product.id],
                    )
                )
        else:
            messages.error(
                request,
                f'Unable to update {product.name}. \
                Please ensure all fields are filled out correctly.'
                )
    else:
        form = WineForm()

    form = WineForm(instance=product)

    messages.info(request, f'You are currently editing {product.name}')

    context = {
        'form': form,
        'wines': wines,
        'product': product,
    }

    return render(
        request,
        'products/edit-product.html',
        context
        )


def edit_works(request, product_id):
    """ Edit the item in the bundles model """
    bundle = Bundle.objects.all()
    product = get_object_or_404(Bundle, pk=product_id)

    if request.method == 'POST':
        form = WorksForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.name}')
            return redirect(
                reverse(
                    'product_details_bundles',
                    args=[product.id],
                    )
                )
        else:
            messages.error(
                request,
                f'Unable to update {product.name}. \
                Please ensure all fields are filled out correctly.'
                )
    else:
        form = WorksForm()

    form = WorksForm(instance=product)

    messages.info(request, f'You are currently editing {product.name}')

    context = {
        'form': form,
        'bundle': bundle,
        'product': product,
    }

    return render(
        request,
        'products/edit-product.html',
        context
        )
