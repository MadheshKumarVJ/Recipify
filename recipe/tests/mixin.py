from django.contrib.auth.models import User
from django.test import TestCase

from recipe.models.recipe import Recipe


class ModelMixin(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="maddy",
            password="123",
        )

    def create_recipes(self, count):
        recipies = []
        for i in range(count):
            recipe = Recipe.objects.create(
                title="test",
                author=self.user,
                instructions="Testing recipe",
                calories=123,
                slug="slug" + str(i),
                preparation_time="123",
            )
            recipies.append(recipe)
        return recipies
