from django.test import TestCase, Client
from django.urls import reverse

from ..models import Dishes


class TestTheMenuView(TestCase):
    """ Test product application views """

    def setUp(self):
        """ Set up """
        self.client = Client()
        self.list_url = reverse('the_menu')

        dish_a = Dishes(
            name='dish 1',
            slug_name='dish-1',
            status=1,
            description='Long description on dish 1',
            price=10.00
        )

        dish_a.save()
        self.dish_a = dish_a

        dish_b = Dishes(
            name='dish 2',
            slug_name='dish-2',
            status=0,
            description='Long description on dish 2',
            price=5.00
        )

        dish_b.save()
        self.dish_b = dish_b

    def test_the_menu_view_renders_correctly(self):
        """ Test the menu view renders """

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/the-menu.html')
    
    def test_if_dishes_exist_in_database(self):
        """ Test to see if the dishes saved in the database """

        dish_count = Dishes.objects.all().count()
        self.assertEqual(dish_count, 2)
