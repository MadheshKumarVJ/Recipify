from django.test import TestCase
from django.urls import reverse

from recipe.tests.mixin import ModelMixin


class TestListView(TestCase):
    def test_list_view_loads_three_posts_per_page(self):
        response = self.client.get(reverse("dashboard"))
        print(response.context)
