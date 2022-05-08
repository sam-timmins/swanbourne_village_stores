from django.shortcuts import render, get_object_or_404

from checkout.models import Order


def orders(request):
    """ A view to return the orders
    """
    orders = Order.objects.all().order_by('-date').order_by('status')

    context = {
        'orders': orders,
        }
    return render(request, 'orders/orders.html', context)


def order_details(request, order_number):
    """ Order details for admin """

    order = get_object_or_404(Order, order_number=order_number)

    context = {
        'order': order,
    }

    return render(request, 'orders/orders_details.html', context)
