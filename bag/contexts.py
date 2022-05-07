from django.shortcuts import get_object_or_404

from products.models import Dishes, Wines, Bundle


def bag_contents(request):
    """
    Calculates the grand total
    """

    bag_items = []
    total = int(0)
    product_count = int(0)
    bag = request.session.get('bag', {})

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
        elif item_slug in bundle_slug_list:
            product = get_object_or_404(Bundle, slug_name=item_slug)
            total += quantity * product.price
            product_count += quantity
            bag_items.append({
                'item_slug': item_slug,
                'quantity': quantity,
                'product': product,
            })

    grand_total = total

    contexts = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return contexts
