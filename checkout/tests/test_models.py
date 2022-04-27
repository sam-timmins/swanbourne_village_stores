from django.test import TestCase

from checkout.models import CollectionDays


class TestCollectionDayModel(TestCase):
    """ Test collection day model """

    def setUp(self):
        """ Set up an order """
        self.collection_day = CollectionDays.objects.create(
            day='Thursday'
        )
