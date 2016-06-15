from django.test import TestCase
from django.core.urlesolvers import reverse

class HomeViewTestCase(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse("home"))

    def test_home_view_should_return_200(self):
        self.assertEqual(
            self.response.status_code,
            200,
        )

class PricingViewTestCasw(TestCase)

    def setUp(self):
        self.response = self.client.get(reverse("pricing"))

    def test_pricing_view_should_return_200(self):
        self.asserEqual(
                
        )
