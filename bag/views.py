from django.shortcuts import render, redirect


def view_bag(request):
    """ A view to return the bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_slug):
    """ Add a quantity of a product to the bag during a session """

    quantity = int(request.POST.get('item-quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_slug in list(bag.keys()):
        bag[item_slug] += quantity
    else:
        bag[item_slug] = quantity

    request.session['bag'] = bag

    print(request.session['bag'])

    return redirect(redirect_url)
