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
            order_number=12345678910,
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

    def test_collection_day_exists(self):
        """ Test the collection day was created """
        count_days = CollectionDays.objects.all().count()
        count_orders = Order.objects.all().count()
        self.assertEqual(count_days, 1)
        self.assertEqual(count_orders, 1)
