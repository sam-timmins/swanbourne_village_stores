from django.test import TestCase, Client
from django.urls import reverse


class TestTheMenuView(TestCase):
    """ Test product application views """

    def setUp(self):
        """ Set up """
        self.client = Client()
        self.list_url = reverse('the_menu')
