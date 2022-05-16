from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from checkout.models import Order, CollectionDays

from .forms import (UpdateStatusForm,
                    CreateCollectionDayForm,
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


def collection_days(request):
    """ A view to return the collection days with the ability to
    create a new collection day on a post request
    """
    days = CollectionDays.objects.all()
    form = CreateCollectionDayForm()

    if request.method == 'POST':
        form = CreateCollectionDayForm(request.POST)
        if form.is_valid():
            day = form.cleaned_data.get('day')
            form.save()
            messages.success(request, f'Successfully added {day} to the \
                available collection days')
            return redirect(reverse('collection_days'))

    context = {
        'days': days,
        'form': form,
        }

    return render(request, 'orders/collection-days.html', context)


def delete_collection_day(request, pk):
    """
    Deletes a collection day based on the pk if there are
    no open orders against the day
    """
    day = CollectionDays.objects.get(pk=pk)
    all_orders = Order.objects.filter(status=0)

    day = str(day).lower()

    order_list = []
    for order in all_orders:
        collection_day = str(order.collection_day).lower()
        order_list.append(collection_day)

    if day in order_list:
        messages.error(request, 'There are open orders against. \
            Please complete all orders due and then delete')
        return redirect('collection_days')
    else:
        day = CollectionDays.objects.get(pk=pk)
        day.delete()
        messages.success(request, 'Collection day successfully deleted.')
        return redirect('collection_days')
