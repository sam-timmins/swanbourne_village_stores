import stripe
import json

from django.views.decorators.http import require_POST
from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404, HttpResponse)
from django.contrib import messages
from django.conf import settings

from products.models import Dishes, Wines, Bundle
from bag.contexts import bag_contents
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
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
        }
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid

            order.original_bag = json.dumps(bag)
            order.save()

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

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
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

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
            }

            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

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


@require_POST
def cache_checkout_data(request):
    """
    Determin if the user has the save-info box checked and add
    to the metadata for the payment intent
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as exception:
        messages.error(request, ('Sorry, your payment cannot be '
                                 'processed right now. Please try '
                                 'again later.'))
        return HttpResponse(content=exception, status=400)
