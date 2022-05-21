from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import Dishes
from products.forms import DishForm


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

    return render(request, 'administration/create-dish.html', context)


@login_required
def delete_dish_product(request, dish_id):
    """Delete dish product"""
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    product = get_object_or_404(Dishes, pk=dish_id)
    product.delete()

    messages.success(request, 'The dish has been deleted from the store')
    return redirect(reverse('dishes'))
