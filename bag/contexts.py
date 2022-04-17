from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404

from products.models import Dishes


def bag_contents(request):
    """
    Bag and ordering variables
    Caluclates free delivery if total is greater than
    FREE_DELIVERY_THRESHOLD or adds 10 percent onto total if
    not
    Calculates the grand total
    """

    bag_items = []
    total = int(0)
    product_count = int(0)
    bag = request.session.get('bag', {})

    for item_slug, quantity in bag.items():
        print(item_slug)
        product = get_object_or_404(Dishes, slug_name=item_slug)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_slug': item_slug,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(
            settings.STANDARD_DELIVERY_PERCENTAGE/int(100)
            )
        free_delivery = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = int(0)
        free_delivery = int(0)

    grand_total = delivery + total

    contexts = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery': free_delivery,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return contexts
