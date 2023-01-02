from django.db.models import Count
from django.test import TestCase
from django.urls import reverse

from recipe.tests.mixin import ModelMixin


class TestListView(ModelMixin, TestCase):
    def test_list_view_loads_three_posts_per_page(self):
        self.create_recipes(count=5)
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(len(response.context["recipies"]), 3)
