from django.shortcuts import render


def view_bag(request):
    """ A view to return the bag page """

    bag_items = 'item'

    context = {
        'bag_items': bag_items,
    }

    return render(
        request,
        'bag/bag.html',
        context
        )
