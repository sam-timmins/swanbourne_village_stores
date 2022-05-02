from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm


def checkout(request):
    """
    Checkout page view with order form it there are items in the
    session and a error message if the bag is empty and the url
    is forced
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'Your basket is currently empty')
        return redirect(reverse('the_menu'))

    order_form = OrderForm()

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': stripe_secret_key,

    }
    return render(request, 'checkout/checkout.html', context)
