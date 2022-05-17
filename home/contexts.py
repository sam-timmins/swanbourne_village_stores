from checkout.models import Order


def site_contexts(request):
    """ Site contexts variables """

    open_orders_count = Order.objects.all().filter(status=0).count()

    completed_orders_not_collected = Order.objects.all().filter(
        status=1).filter(collected_order=0).count()

    completed_orders_and_collected = Order.objects.all().filter(
        status=1).filter(collected_order=1).count()

    store_name = 'Swanbourne Village Stores'
    currency = '£'
    store_email = 'swanbourne.store@gmail.com'
    store_phone_number = '+441296720288'
    store_dropped_pin = 'https://www.google.com/maps/place/5+Mursley+Rd, \
        +Swanbourne,+Milton+Keynes+MK17+0SH,+UK/@51.938599,-0.836613,17z/ \
        data=!3m1!4b1!4m5!3m4!1s0x4876fecc061ac491:0xdcf505f1debf6cae!8m \
        2!3d51.9385957!4d-0.8344243'
    facebook = 'https://www.facebook.com/SwanbourneStores'
    instagram = 'https://www.instagram.com/'
    twitter = 'https://www.twitter.com/'

    placeholder_image_url = 'https://res.cloudinary.com/sam-timmins1/image/upload/v1648242080/static/images/hero.b0249628474d.jpg' # noqa

    contexts = {
        'store_name': store_name,
        'currency': currency,
        'facebook': facebook,
        'instagram': instagram,
        'twitter': twitter,
        'store_dropped_pin': store_dropped_pin,
        'store_phone_number': store_phone_number,
        'store_email': store_email,
        'placeholder_image_url': placeholder_image_url,
        'open_orders_count': open_orders_count,
        'completed_orders_not_collected': completed_orders_not_collected,
        'completed_orders_and_collected': completed_orders_and_collected,
    }

    return contexts
