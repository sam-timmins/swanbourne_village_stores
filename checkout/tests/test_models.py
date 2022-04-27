from django.test import TestCase

from checkout.models import CollectionDays


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
