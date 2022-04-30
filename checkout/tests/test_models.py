import uuid

from django.test import TestCase
import datetime

from checkout.models import CollectionDays, Order


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
        self.collection_day = CollectionDays.objects.create(
            day='Thursday'
        )

        self.order_one = Order.objects.create(
            order_number='',
            full_name='Sam Timmins',
            email='sam@email.com',
            phone_number=1234567890,
            collection_day=CollectionDays.objects.get(id=1),
            country='Ireland',
            postcode='A82E4T8',
            town_or_city='Cavan',
            street_address1='Main street',
            street_address2='',
            county='Cavan',
            date=datetime.datetime.now(),
            delivery_cost=10,
            order_total=100,
            grand_total=110,
        )

        self.order_two = Order.objects.create(
            order_number='',
            full_name='AN Other',
            email='another@email.com',
            phone_number=1234567890,
            collection_day=CollectionDays.objects.get(id=1),
            country='Ireland',
            postcode='A86TRT8',
            town_or_city='Ballyjamesduff',
            street_address1='Cavan Road',
            street_address2='',
            county='Cavan',
            date=datetime.datetime.now(),
            delivery_cost=15,
            order_total=150,
            grand_total=165,
        )

    def test_collection_day_exists(self):
        """ Test the collection day and order were created """
        count_days = CollectionDays.objects.all().count()
        count_orders = Order.objects.all().count()
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
