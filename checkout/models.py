import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

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
    date = models.DateTimeField(
        auto_now_add=True
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
    original_bag = models.TextField(
        null=False,
        blank=False,
        default=''
        )
    stripe_pid = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default=''
        )

    def __str__(self):
        return f'{self.order_number}'

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a order item is added
        """
        self.order_total = self.orderitems.aggregate(Sum('orderitem_total'))['orderitem_total__sum'] or 0

        self.grand_total = self.order_total
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)


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

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the orderitem total
        and update the order total depending on if the.
        """
        if self.dish or self.wine or self.bundle:
            if self.dish:
                self.orderitem_total = self.dish.price * self.quantity
                super().save(*args, **kwargs)
            elif self.wine:
                self.orderitem_total = self.wine.price * self.quantity
                super().save(*args, **kwargs)
            else:
                self.orderitem_total = self.bundle.price * self.quantity
                super().save(*args, **kwargs)
        else:
            return

    def __str__(self):
        return f'{self.order}'
