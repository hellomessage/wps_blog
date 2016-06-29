from django.test import TestCase
from django.core.urlesolvers import reverse


class PricingViewTestCase(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse("pricing"))

    def test_pricing_view_should_return_200(self):
        """
        pricing으로 접속했을 때, status code가 200 ok가 나와야 한다.
        """
        self.assertEqual(
            self.response.status_code,
            200,
        )

    def test_pricing_view_should_have_good_title(self):
        """
        pricing으로 접속했을 때, response에 "Priving Table" 이라는 텍스트가 포함되어야 한다.
        """
        self.assertContains(
            self.response,
            "Priving Table",
        )
