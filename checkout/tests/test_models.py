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

    def test_collection_day_string_length_is_less_than_or_equal_to_nine(self):
        """ Test string length of collection day """
        self.assertLessEqual(len(self.collection_day.day), 9)
