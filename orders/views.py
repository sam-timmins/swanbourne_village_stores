from django.shortcuts import render


def orders(request):
    """ A view to return the orders
    """
    return render(request, 'orders/orders.html')
