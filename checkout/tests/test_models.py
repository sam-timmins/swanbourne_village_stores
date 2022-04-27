from django.test import TestCase

from checkout.models import CollectionDays


class TestCollectionDayModel(TestCase):
    """ Test collection day model """

    def setUp(self):
        """ Set up a collection day """
        self.collection_day = CollectionDays.objects.create(
            day='Thursday'
        )
