from django.test import TestCase, Client
from django.urls import reverse


class TestTheMenuView(TestCase):
    """ Test product application views """

    def setUp(self):
        """ Set up """
        self.client = Client()
        self.list_url = reverse('the_menu')

    def test_the_menu_view_renders_correctly(self):
        """ Test the menu view renders """

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/the-menu.html')
