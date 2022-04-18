from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404

from products.models import Dishes, Wines


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

    dishes = Dishes.objects.all()
    wines = Wines.objects.all()
    dish_slug_list = []
    wine_slug_list = []

    for dish in dishes:
        dish_slug_list.append(dish.slug_name)

    for wine in wines:
        wine_slug_list.append(wine.slug_name)

    for item_slug, quantity in bag.items():

        if item_slug in dish_slug_list:
            product = get_object_or_404(Dishes, slug_name=item_slug)
            total += quantity * product.price
            product_count += quantity
            bag_items.append({
                'item_slug': item_slug,
                'quantity': quantity,
                'product': product,
            })
        elif item_slug in wine_slug_list:
            product = get_object_or_404(Wines, slug_name=item_slug)
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
