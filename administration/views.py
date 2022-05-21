from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import Dishes, Wines, Bundle
from products.forms import WorksForm

from .forms import DishForm, WineForm


def administration(request):
    """ A view to return the privacy policy """

    return render(request, 'administration/administration.html')


@login_required
def dishes(request):
    """ Add a dish to the store """
    if not request.user.is_superuser:
        messages.info(request, 'Only store owners can create a dish')
        return redirect(reverse('home'))

    dishes = Dishes.objects.all()
    count_dishes = Dishes.objects.all().count()

    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            format_name = name.title()
            form.save()
            messages.success(request, f'Successfully created {format_name}')
            return redirect(reverse('dishes'))
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
        'dishes': dishes,
        'count_dishes': count_dishes,
    }

    return render(request, 'administration/dishes.html', context)


@login_required
def delete_dish_product(request, dish_id):
    """Delete dish product"""
    if not request.user.is_superuser:
        messages.info(request, 'Only store owners can delete a dish')
        return redirect(reverse('home'))

    product = get_object_or_404(Dishes, pk=dish_id)
    product.delete()

    messages.success(request, 'The dish has been deleted from the store')
    return redirect(reverse('dishes'))


@login_required
def edit_dish(request, dish_id):
    """ Edit the item in the dishes model """
    if not request.user.is_superuser:
        messages.info(request, 'Only store owners can edit a dish')
        return redirect(reverse('home'))

    dishes = Dishes.objects.all()
    product = get_object_or_404(Dishes, pk=dish_id)

    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.name}')
            return redirect(reverse('dishes'))
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
        'components/edit/edit-dish.html',
        context
        )


@login_required
def wines(request):
    """ Add a dish to the store """
    if not request.user.is_superuser:
        messages.info(request, 'Only store owners can create a wine')
        return redirect(reverse('home'))

    wines = Wines.objects.all()
    count_wines = Wines.objects.all().count()

    if request.method == 'POST':
        form = WineForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            format_name = name.title()
            form.save()
            messages.success(request, f'Successfully created {format_name}')
            return redirect(reverse('wines'))
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
        'wines': wines,
        'count_wines': count_wines,
    }

    return render(request, 'administration/wines.html', context)


@login_required
def delete_wine_product(request, wine_id):
    """Delete wine product"""
    if not request.user.is_superuser:
        messages.info(request, 'Only store owners can delete a wine')
        return redirect(reverse('home'))

    product = get_object_or_404(Wines, pk=wine_id)
    product.delete()

    messages.success(request, 'The wine has been deleted from the store')
    return redirect(reverse('wines'))


@login_required
def edit_wine(request, wine_id):
    """ Edit the item in the wines model """
    if not request.user.is_superuser:
        messages.info(request, 'Only store owners can edit a wine')
        return redirect(reverse('home'))

    wines = Wines.objects.all()
    product = get_object_or_404(Wines, pk=wine_id)

    if request.method == 'POST':
        form = WineForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.name}')
            return redirect(reverse('wines'))
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
        'components/edit/edit-wine.html',
        context
        )


@login_required
def works(request):
    """ Add a dish to the store """
    if not request.user.is_superuser:
        messages.info(request, 'Only store owners can create the works')
        return redirect(reverse('home'))

    the_works = Bundle.objects.all()
    dishes = Dishes.objects.all()
    wines = Wines.objects.all()
    count_works = Bundle.objects.all().count()

    if request.method == 'POST':
        form = WorksForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            format_name = name.title()
            form_dish = form.cleaned_data.get('dish')
            form_wine = form.cleaned_data.get('wine')
            form_price = form.cleaned_data.get('price')

            for dish in dishes:
                if form_dish == dish:
                    dish_price = dish.price
            for wine in wines:
                if form_wine == wine:
                    wine_price = wine.price

            total = dish_price + wine_price

            if total <= form_price:
                messages.error(request, 'There was no discount on this \
                    combination so it was not saved')
                return redirect(reverse('works'))

            form.save()
            messages.success(request, f'Successfully created {format_name}')
            return redirect(reverse('works'))
        else:
            messages.error(
                request,
                'Unable to create the dish. \
                Please ensure all fields are filled out correctly.'
                )
    else:
        form = WorksForm()

    context = {
        'form': form,
        'the_works': the_works,
        'count_works': count_works,
    }

    return render(request, 'administration/works.html', context)


@login_required
def delete_works_product(request, works_id):
    """Delete works product"""
    if not request.user.is_superuser:
        messages.info(request, 'Only store owners can delete a works')
        return redirect(reverse('home'))

    product = get_object_or_404(Bundle, pk=works_id)
    product.delete()

    messages.success(request, 'The works has been deleted from the store')
    return redirect(reverse('works'))


@login_required
def edit_works(request, works_id):
    """ Edit the item in the works model """
    if not request.user.is_superuser:
        messages.info(request, 'Only store owners can edit the works')
        return redirect(reverse('home'))

    works = Bundle.objects.all()
    product = get_object_or_404(Bundle, pk=works_id)

    if request.method == 'POST':
        form = WorksForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.name}')
            return redirect(reverse('works'))
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
        'works': works,
        'product': product,
    }

    return render(
        request,
        'components/edit/edit-works.html',
        context
        )