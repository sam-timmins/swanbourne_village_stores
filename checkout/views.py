import stripe

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from bag.contexts import bag_contents
from .forms import OrderForm


def checkout(request):
    """
    Checkout page view with order form it there are items in the
    session and a error message if the bag is empty and the url
    is forced
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'collection_day': request.POST['collection_day'],
            # 'country': request.POST['country'],
            # 'postcode': request.POST['postcode'],
            # 'town_or_city': request.POST['town_or_city'],
            # 'street_address1': request.POST['street_address1'],
            # 'street_address2': request.POST['street_address2'],
            # 'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)

        print(form_data)

    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, 'Your basket is currently empty')
            return redirect(reverse('the_menu'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)

        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
            )

        order_form = OrderForm()

        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,

        }
        return render(request, 'checkout/checkout.html', context)
