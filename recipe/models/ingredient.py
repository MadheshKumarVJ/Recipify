from django.db import models

from .recipe import Recipe


class Ingredient(models.Model):

    name = models.CharField(max_length=250)
    quantity = models.CharField(max_length=50)
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredients"
    )
    optional = models.BooleanField(default=False)

    class Meta:
        app_label = "recipe"

    def __str__(self):
        return self.name
