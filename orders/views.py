from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from checkout.models import Order

from .forms import UpdateStatusForm


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

    form = UpdateStatusForm(data=request.POST)

    if form.is_valid():

        update = form.save(commit=False)

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
        form = UpdateStatusForm()

    context = {
        'order': order,
        'form': form,
    }

    return render(request, 'orders/orders_details.html', context)


def delete_order(request, order_number):
    """ Deletes an order based on the order number"""
    order = Order.objects.get(order_number=order_number)
    order.delete()

    messages.success(request, 'Order successfully deleted.')

    return redirect('orders')
