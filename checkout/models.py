from django.db import models

from products.models import Dishes, Wines, Bundle


class CollectionDays(models.Model):
    """ Model for colection days """
    day = models.CharField(
        max_length=9,
        unique=True,
        blank=False,
    )

    def __str__(self):
        return f'{self.day}'


class Order(models.Model):
    """ Model for an order """

    order_number = models.CharField(
        max_length=32,
        null=False,
        editable=False
        )
    full_name = models.CharField(
        max_length=50,
        null=False,
        blank=False
        )
    email = models.EmailField(
        max_length=254,
        null=False,
        blank=False
        )
    phone_number = models.CharField(
        max_length=20,
        null=False,
        blank=False
        )
    collection_day = models.ForeignKey(
        CollectionDays,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        )
    country = models.CharField(
        max_length=40,
        null=False,
        blank=False
        )
    postcode = models.CharField(
        max_length=20,
        blank=True
        )
    town_or_city = models.CharField(
        max_length=40,
        null=False,
        blank=False
        )
    street_address1 = models.CharField(
        max_length=80,
        null=False,
        blank=False
        )
    street_address2 = models.CharField(
        max_length=80,
        blank=True
        )
    county = models.CharField(
        max_length=80,
        blank=True
        )
    date = models.DateTimeField(
        auto_now_add=True
        )
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False,
        default=0
        )
    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
        )
    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
        )

    def __str__(self):
        return f'{self.order_number}'


class OrderItem(models.Model):
    """ Model for individual order item """
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='orderitems'
        )
    dish = models.ForeignKey(
        Dishes,
        null=True,
        blank=True,
        on_delete=models.CASCADE
        )
    wine = models.ForeignKey(
        Wines,
        null=True,
        blank=True,
        on_delete=models.CASCADE
        )
    bundle = models.ForeignKey(
        Bundle,
        null=True,
        blank=True,
        on_delete=models.CASCADE
        )
    quantity = models.IntegerField(
        null=False,
        blank=False,
        default=0
        )
    orderitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False
        )

    def __str__(self):
        return f'{self.order}'
