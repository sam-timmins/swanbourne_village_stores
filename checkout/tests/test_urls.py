from django.test import TestCase
from django.urls import reverse, resolve
from checkout.views import checkout, checkout_success


class TestUrls(TestCase):
    """ Test the response of the checkout app's URLs """

    def test_response_of_checkout_page(self):
        """ Test the response of the checkout URL """
        url = reverse('checkout')
        self.assertEqual(resolve(url).func, checkout)

    def test_response_of_checkout_success_page(self):
        """ Test the response of the checkout success URL """
        url = reverse('checkout_success', args=['THD3591GER'])
        self.assertEqual(resolve(url).func, checkout_success)
