from django.test import TestCase
from django.urls import reverse, resolve
from checkout.views import checkout


class TestUrls(TestCase):
    """ Test the response of the checkout app's URLs """

    def test_response_of_checkout_page(self):
        """ Test the response of the checkout URL """
        url = reverse('checkout')
        self.assertEqual(resolve(url).func, checkout)
