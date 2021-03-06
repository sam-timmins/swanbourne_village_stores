import uuid
import datetime

from django.test import TestCase

from checkout.models import CollectionDays, Order, OrderItem
from products.models import Dishes


class TestCollectionDayModel(TestCase):
    """ Test collection day model """

    def setUp(self):
        """ Set up a collection day """
        self.collection_day = CollectionDays.objects.create(
            day='Thursday'
        )

    def test_collection_day_exists(self):
        """ Test the collection day was created """
        count_days = CollectionDays.objects.all().count()
        self.assertEqual(count_days, 1)

    def test_collection_day_string_length_is_less_than_or_equal_to_nine(self):
        """ Test string length of collection day """
        self.assertLessEqual(len(self.collection_day.day), 9)


class TestOrderModel(TestCase):
    """ Test the order model """

    def setUp(self):
        """ Model setup """
        self.chicken_dinner = Dishes.objects.create(
            name='Chicken dinner',
            slug_name='chicken_dinner',
            description='A chicken dinner',
            price=10.99,
            status=1,
        )

        self.vegetable_dinner = Dishes.objects.create(
            name='Vegetable dinner',
            slug_name='vegetable_dinner',
            description='A chicken dinner',
            price=10.99,
            status=1,
        )

        self.collection_day = CollectionDays.objects.create(
            day='Thursday'
        )

        self.order_one = Order.objects.create(
            order_number='',
            full_name='Sam Timmins',
            email='sam@email.com',
            phone_number=1234567890,
            collection_day=CollectionDays.objects.get(id=1),
            date=datetime.datetime.now(),
            order_total=0,
            grand_total=0,
        )

        self.order_two = Order.objects.create(
            order_number='',
            full_name='AN Other',
            email='another@email.com',
            phone_number=1234567890,
            collection_day=CollectionDays.objects.get(id=1),
            date=datetime.datetime.now(),
            order_total=150,
            grand_total=150,
        )

        self.order_item_one = OrderItem.objects.create(
            order=self.order_one,
            dish=self.chicken_dinner,
            quantity=10,
            orderitem_total=0,
        )

    def test_collection_day_and_order_exists(self):
        """ Test the collection day and order were created """
        count_days = CollectionDays.objects.all().count()
        count_orders = Order.objects.all().count()
        count_dishes = Dishes.objects.all().count()
        self.assertEqual(count_dishes, 2)
        self.assertEqual(count_days, 1)
        self.assertEqual(count_orders, 2)

    def test_a_unique_order_number_is_created_and_saved(self):
        """ Test order number is created to the correct length, unique
        and saved to an order order
        """
        generated_order_number_order_one = uuid.uuid4().hex.upper()
        generated_order_number_order_two = uuid.uuid4().hex.upper()
        self.assertEqual(len(generated_order_number_order_one), 32)
        self.order_one.order_number = generated_order_number_order_one
        self.order_one.save()
        self.assertEqual(
            self.order_one.order_number,
            generated_order_number_order_one
            )
        self.assertNotEqual(
            generated_order_number_order_one,
            generated_order_number_order_two
            )

    def test_order_item_model_product_foreign_key_is_not_blank(self):
        """ Test the order item model """
        if self.order_item_one.dish or \
                self.order_item_one.wine or \
                self.order_item_one.bundle:
            self.assertTrue(self.order_item_one.dish)
        else:
            self.assertFalse(self.order_item_one.dish)
            self.assertFalse(self.order_item_one.wine)
            self.assertFalse(self.order_item_one.bundle)

    def test_order_item_model_to_update_order_total(self):
        """
        Test order item model to check if the product is
        in the Dishes model. Multipy the price of the dish by the
        quantity and save the order total
        """
        self.assertTrue(self.order_item_one.dish)
        self.assertFalse(self.order_item_one.wine)
        if self.order_item_one.dish:
            self.order_item_one.orderitem_total = \
                self.order_item_one.dish.price * \
                self.order_item_one.quantity
            self.order_one.order_total = self.order_item_one.orderitem_total
            self.order_one.save()
            self.assertEqual(
                self.order_one.order_total,
                self.order_item_one.orderitem_total
                )
            self.assertEqual(self.order_item_one.orderitem_total, 109.90)
