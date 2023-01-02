from django.db import models

from .recipe import Recipe


class Ingredient(models.Model):

    CHOICES = (
        ("needed", "Needed"),
        ("optional", "Optional"),
    )
    name = models.CharField(max_length=250)
    quantity = models.IntegerField()
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredients"
    )
    optional = models.CharField(max_length=10, choices=CHOICES, default="needed")

    class Meta:
        app_label = "recipe"

    def __str__(self):
        return self.name
