from django.shortcuts import render, redirect
from django.contrib import messages


def view_bag(request):
    """ A view to return the bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_slug):
    """ Add a quantity of a product to the bag during a session """

    quantity = int(request.POST.get('item-quantity'))
    redirect_url = request.POST.get('redirect_url')
    product_name = request.POST.get('product_name')
    bag = request.session.get('bag', {})

    if item_slug in list(bag.keys()):
        bag[item_slug] += quantity
        if quantity > 1:
            messages.success(
                request,
                f'{quantity} {product_name} dishes added to the basket'
                )
        else:
            messages.success(
                request,
                f"{quantity} {product_name} dish added to the basket"
                )
    else:
        bag[item_slug] = quantity

    request.session['bag'] = bag

    return redirect(redirect_url)
