from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from itertools import chain

from products.models import Dishes, Wines, Bundle


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

    for item_id, quantity in bag.items():
        product = get_object_or_404(Dishes, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
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
