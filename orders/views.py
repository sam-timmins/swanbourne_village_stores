from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from checkout.models import Order

from .forms import (UpdateStatusForm,
                    UpdateCollectionStatusForm,
                    )


def orders(request):
    """ A view to return the orders
    """
    orders = Order.objects.all().order_by('status', 'collected_order')

    if request.GET:
        if 'order' in request.GET:
            order = request.GET['order']
            if order == 'collected':
                orders = orders.filter(collected_order=1)
            elif order == 'not_collected':
                orders = orders.filter(collected_order=0)
            elif order == 'open':
                orders = orders.filter(status=0)
            elif order == 'complete':
                orders = orders.filter(status=1)

    context = {
        'orders': orders,
        }
    return render(request, 'orders/orders.html', context)


def order_details(request, order_number):
    """ Order details for admin """

    order = get_object_or_404(Order, order_number=order_number)

    status_form = UpdateStatusForm(data=request.POST)
    collected_form = UpdateCollectionStatusForm(data=request.POST)

    if status_form.is_valid():

        update = status_form.save(commit=False)

        status = request.POST['status']

        update.order = order
        order.status = status
        order.save()
        messages.success(request, 'Order successfully updated')

        return redirect(reverse(
            'order_details',
            args=[order.order_number])
            )

    else:
        status_form = UpdateStatusForm()

    if collected_form.is_valid():

        update = collected_form.save(commit=False)

        collected_status = request.POST['collected_order']

        update.order = order
        order.collected_order = collected_status
        order.save()
        messages.success(request, 'Collection status of the order \
            successfully updated')

        return redirect(reverse(
            'order_details',
            args=[order.order_number])
            )

    else:
        collected_form = UpdateCollectionStatusForm()

    context = {
        'order': order,
        'status_form': status_form,
        'collected_form': collected_form,
    }

    return render(request, 'orders/orders_details.html', context)


def delete_order(request, order_number):
    """ Deletes an order based on the order number"""
    order = Order.objects.get(order_number=order_number)
    order.delete()

    messages.success(request, 'Order successfully deleted.')

    return redirect('orders')
