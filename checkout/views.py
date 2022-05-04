import stripe

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from products.models import Dishes, Wines, Bundle
from bag.contexts import bag_contents
from .forms import Order, OrderForm
from .models import OrderItem


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

        if order_form.is_valid():
            order = order_form.save()

            dishes = Dishes.objects.all()
            wines = Wines.objects.all()
            bundles = Bundle.objects.all()

            dish_slug_list = []
            wine_slug_list = []
            bundle_slug_list = []

            for dish in dishes:
                dish_slug_list.append(dish.slug_name)

            for wine in wines:
                wine_slug_list.append(wine.slug_name)

            for bundle in bundles:
                bundle_slug_list.append(bundle.slug_name)

            for item_slug, item_data in bag.items():
                try:
                    if item_slug in dish_slug_list:
                        dish = Dishes.objects.get(slug_name=item_slug)
                        order_item = OrderItem(
                            order=order,
                            dish=dish,
                            quantity=item_data,
                        )
                        order_item.save()
                    if item_slug in wine_slug_list:
                        wine = Wines.objects.get(slug_name=item_slug)
                        order_item = OrderItem(
                            order=order,
                            wine=wine,
                            quantity=item_data,
                        )
                        order_item.save()
                    if item_slug in bundle_slug_list:
                        bundle = Bundle.objects.get(slug_name=item_slug)
                        order_item = OrderItem(
                            order=order,
                            bundle=bundle,
                            quantity=item_data,
                        )
                        order_item.save()
                except (
                        Dishes.DoesNotExist,
                        Wines.DoesNotExist,
                        Bundle.DoesNotExist
                        ):
                    messages.error(request, 'One of the items in your basket was not found \
                        in our database. Please contact us for assistance.')
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success',
                args=[order.order_number])
                )
        else:
            messages.error(request, 'There was an error with your order form. \
                Please double check your information.')
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


def checkout_success(request, order_number):
    """ Handles successful checkouts """
    dishes = Dishes.objects.all()
    wines = Wines.objects.all()
    bundles = Bundle.objects.all()

    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Your order ({order_number}) has been \
        successfully processed. We have sent you a confirmation email \
            to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    context = {
        'order': order,
        'dishes': dishes,
        'wines': wines,
        'bundles': bundles,
    }

    return render(request, 'checkout/checkout-success.html', context)
