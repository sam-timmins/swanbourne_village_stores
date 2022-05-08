from django.shortcuts import render

from checkout.models import Order


def orders(request):
    """ A view to return the orders
    """
    orders = Order.objects.all().order_by('-date')

    context = {
        'orders': orders,
        }
    return render(request, 'orders/orders.html', context)
