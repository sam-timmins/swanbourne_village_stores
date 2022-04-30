from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Calculates the sub total based on the product's
    price and quantity
    """
    return price * quantity
